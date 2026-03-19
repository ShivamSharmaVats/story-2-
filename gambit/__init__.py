"""Flask application factory and API routes for The Gambit."""

from __future__ import annotations

import json
import os
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

from flask import Flask, jsonify, render_template, request, session

from .game_engine import GameEngine, GameEngineError


SAVE_DIR = Path(__file__).resolve().parent.parent / "instance" / "saves"


def _ensure_session_id() -> str:
    """Return a stable session id for the current browser session."""
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
    return str(session["session_id"])


def _json_error(message: str, status: int = 400):
    """Return a normalized error payload."""
    return jsonify({"ok": False, "error": message}), status


def _load_payload() -> dict[str, Any]:
    """Read and validate JSON body."""
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        raise GameEngineError("Request body must be a JSON object.")
    return payload


def create_app() -> Flask:
    """Create and configure the Flask app instance."""
    project_root = Path(__file__).resolve().parent.parent
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder=str(project_root / "templates"),
        static_folder=str(project_root / "static"),
        static_url_path="/static",
    )
    app.config["SECRET_KEY"] = os.environ.get("GAMBIT_SECRET", "dev-secret-change-me")

    SAVE_DIR.mkdir(parents=True, exist_ok=True)

    @app.get("/")
    def index():
        """Main game page."""
        _ensure_session_id()
        return render_template("index.html")

    @app.post("/api/start")
    def start_game():
        """Start a new run from the title screen."""
        engine = GameEngine.from_session(session)
        scene = engine.start_new_game()
        engine.save_to_session(session)
        return jsonify({"ok": True, "state": engine.public_state(), "scene": scene})

    @app.get("/api/state")
    def get_state():
        """Return current game state and active scene."""
        engine = GameEngine.from_session(session)
        if not engine.has_active_game:
            return jsonify({"ok": True, "state": engine.public_state(), "scene": None})
        scene = engine.get_current_scene_payload()
        return jsonify({"ok": True, "state": engine.public_state(), "scene": scene})

    @app.post("/api/choice")
    def choose():
        """Apply a player choice and advance to next scene."""
        try:
            payload = _load_payload()
            choice_id = payload.get("choice_id")
            if not isinstance(choice_id, str) or not choice_id.strip():
                raise GameEngineError("choice_id must be a non-empty string.")

            engine = GameEngine.from_session(session)
            scene = engine.apply_choice(choice_id.strip())
            engine.save_to_session(session)
            return jsonify({"ok": True, "state": engine.public_state(), "scene": scene})
        except GameEngineError as exc:
            return _json_error(str(exc), 400)

    @app.post("/api/restart")
    def restart():
        """Reset current run back to title state."""
        engine = GameEngine.from_session(session)
        engine.restart()
        engine.save_to_session(session)
        return jsonify({"ok": True, "state": engine.public_state(), "scene": None})

    @app.post("/api/save")
    def save_slot():
        """Persist current game state to disk for manual load."""
        engine = GameEngine.from_session(session)
        if not engine.has_active_game:
            return _json_error("No active run to save.", 400)

        slot_id = str(uuid.uuid4())
        filename = SAVE_DIR / f"{slot_id}.json"
        doc = {
            "slot_id": slot_id,
            "saved_at": datetime.utcnow().isoformat() + "Z",
            "state": engine.serialize(),
        }
        filename.write_text(json.dumps(doc, indent=2), encoding="utf-8")

        return jsonify(
            {
                "ok": True,
                "slot": {
                    "slot_id": slot_id,
                    "saved_at": doc["saved_at"],
                },
            }
        )

    @app.get("/api/saves")
    def list_saves():
        """List all save slots available to this local app instance."""
        slots: list[dict[str, str]] = []
        for file in sorted(SAVE_DIR.glob("*.json")):
            try:
                data = json.loads(file.read_text(encoding="utf-8"))
                slots.append(
                    {
                        "slot_id": data.get("slot_id", file.stem),
                        "saved_at": data.get("saved_at", "unknown"),
                    }
                )
            except json.JSONDecodeError:
                continue

        slots.sort(key=lambda item: item["saved_at"], reverse=True)
        return jsonify({"ok": True, "slots": slots})

    @app.post("/api/load")
    def load_slot():
        """Load a save slot into current session."""
        try:
            payload = _load_payload()
            slot_id = payload.get("slot_id")
            if not isinstance(slot_id, str) or not slot_id.strip():
                raise GameEngineError("slot_id must be provided.")

            file = SAVE_DIR / f"{slot_id.strip()}.json"
            if not file.exists():
                raise GameEngineError("Save slot not found.")

            data = json.loads(file.read_text(encoding="utf-8"))
            state = data.get("state")
            if not isinstance(state, dict):
                raise GameEngineError("Save file is corrupted.")

            engine = GameEngine.deserialize(state)
            engine.save_to_session(session)
            scene = engine.get_current_scene_payload() if engine.has_active_game else None
            return jsonify({"ok": True, "state": engine.public_state(), "scene": scene})
        except (GameEngineError, json.JSONDecodeError) as exc:
            return _json_error(str(exc), 400)

    return app
