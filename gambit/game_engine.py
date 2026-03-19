"""Core game engine for The Gambit.

The engine is intentionally separated from Flask routes so it can be tested and
expanded independently.
"""

from __future__ import annotations

from typing import Any

from .models import Choice, GameState, Scene
from .story_data import START_SCENE_ID, build_story


class GameEngineError(Exception):
    """Raised for invalid game operations."""


class GameEngine:
    """Stateful scene/choice engine for the branching story."""

    SESSION_KEY = "gambit_state"

    def __init__(self, state: GameState | None = None):
        self.story: dict[str, Scene] = build_story()
        self.state = state or GameState()

        # Validate that configured scene ids are real, failing fast in development.
        self._validate_story_integrity()

    @property
    def has_active_game(self) -> bool:
        """True when a run has started and a valid current scene exists."""
        return bool(self.state.started and self.state.current_scene in self.story)

    def start_new_game(self) -> dict[str, Any]:
        """Reset state and start from the canonical first scene."""
        self.state = GameState(
            current_scene=START_SCENE_ID,
            started=True,
            inventory={
                "cash": 0,
                "holy_water": 0,
                "perfect_herb": 0,
                "forgotten_tears": 0,
                "wine_shady": 0,
                "wine_lux": 0,
                "gold_coin": 0,
            },
            flags={},
            path=[],
            endings_seen=[],
            chapters_seen=[],
        )
        return self.get_current_scene_payload()

    def restart(self) -> None:
        """Clear active run while preserving discovered endings for session UX."""
        endings_seen = list(self.state.endings_seen)
        self.state = GameState(endings_seen=endings_seen)

    def apply_choice(self, choice_id: str) -> dict[str, Any]:
        """Apply one choice from the current scene and return next scene payload."""
        if not self.has_active_game:
            raise GameEngineError("No active run. Start the game first.")

        scene = self.story[self.state.current_scene]
        visible_choices = self._visible_choices(scene)

        selected = next((item for item in visible_choices if item.id == choice_id), None)
        if selected is None:
            raise GameEngineError("That choice is unavailable in the current scene.")

        self._record_choice(scene=scene, choice=selected)
        self._apply_effects(selected.effects)

        if selected.next_scene not in self.story:
            raise GameEngineError(f"Story is misconfigured: unknown scene '{selected.next_scene}'.")

        self.state.current_scene = selected.next_scene

        # Resolve auto-continue scenes to avoid dead-end intermediary states.
        self._resolve_auto_continue_chain()

        return self.get_current_scene_payload()

    def get_current_scene_payload(self) -> dict[str, Any]:
        """Return frontend payload for current scene."""
        if not self.has_active_game:
            raise GameEngineError("No active run.")

        scene = self.story[self.state.current_scene]
        self._touch_chapter(scene.chapter)

        choices = [
            {
                "id": choice.id,
                "label": choice.label,
                "note": choice.note,
            }
            for choice in self._visible_choices(scene)
        ]

        payload = {
            "id": scene.id,
            "title": scene.title,
            "chapter": scene.chapter,
            "text": scene.text,
            "tags": scene.tags,
            "choices": choices,
            "ending": scene.ending,
            "is_ending": bool(scene.ending),
            "progress": self._progress_metrics(),
        }

        if scene.ending:
            ending_id = str(scene.ending.get("id", scene.id))
            if ending_id not in self.state.endings_seen:
                self.state.endings_seen.append(ending_id)

        return payload

    def public_state(self) -> dict[str, Any]:
        """Return a safe state payload for frontend HUD and save previews."""
        return {
            "started": self.state.started,
            "current_scene": self.state.current_scene,
            "inventory": self.state.inventory,
            "flags": self.state.flags,
            "path": self.state.path,
            "endings_seen": self.state.endings_seen,
            "chapters_seen": self.state.chapters_seen,
            "stats": {
                "choices_made": len(self.state.path),
                "endings_unlocked": len(self.state.endings_seen),
            },
        }

    def serialize(self) -> dict[str, Any]:
        """Serialize engine state for save slots."""
        return self.state.to_dict()

    @classmethod
    def deserialize(cls, data: dict[str, Any]) -> "GameEngine":
        """Create engine from serialized save data."""
        state = GameState.from_dict(data)
        return cls(state=state)

    def save_to_session(self, session_obj: Any) -> None:
        """Persist current state in Flask session object."""
        session_obj[self.SESSION_KEY] = self.serialize()
        session_obj.modified = True

    @classmethod
    def from_session(cls, session_obj: Any) -> "GameEngine":
        """Hydrate engine from Flask session object."""
        data = session_obj.get(cls.SESSION_KEY)
        if isinstance(data, dict):
            return cls.deserialize(data)
        return cls()

    def _visible_choices(self, scene: Scene) -> list[Choice]:
        """Return scene choices currently available based on state conditions."""
        return [choice for choice in scene.choices if self._conditions_met(choice.conditions)]

    def _conditions_met(self, conditions: dict[str, Any]) -> bool:
        """Evaluate condition payload against current state."""
        if not conditions:
            return True

        required_flags = conditions.get("flags", {})
        for key, expected_value in required_flags.items():
            if self.state.flags.get(key) != expected_value:
                return False

        forbidden_flags = conditions.get("not_flags", [])
        for key in forbidden_flags:
            if bool(self.state.flags.get(key)):
                return False

        required_items = conditions.get("items_at_least", {})
        for item_name, minimum in required_items.items():
            if int(self.state.inventory.get(item_name, 0)) < int(minimum):
                return False

        return True

    def _apply_effects(self, effects: dict[str, Any]) -> None:
        """Apply effects payload to mutable state."""
        if not effects:
            return

        for key, value in effects.get("set_flags", {}).items():
            self.state.flags[key] = value

        for item, delta in effects.get("inc_items", {}).items():
            current = int(self.state.inventory.get(item, 0))
            next_value = current + int(delta)
            self.state.inventory[item] = max(0, next_value)

    def _record_choice(self, scene: Scene, choice: Choice) -> None:
        """Append path record used by ending summary UI."""
        self.state.path.append(
            {
                "scene_id": scene.id,
                "scene_title": scene.title,
                "choice_id": choice.id,
                "choice_label": choice.label,
            }
        )

    def _touch_chapter(self, chapter: str) -> None:
        """Track chapter progression for analytics and replay UX."""
        if chapter and chapter not in self.state.chapters_seen:
            self.state.chapters_seen.append(chapter)

    def _resolve_auto_continue_chain(self) -> None:
        """Advance through auto-continue links until a choice/end scene is reached."""
        guard = 0
        while self.state.current_scene in self.story:
            guard += 1
            if guard > 50:
                raise GameEngineError("Auto-continue loop detected in story graph.")

            scene = self.story[self.state.current_scene]
            if not scene.auto_continue_to:
                break

            if scene.auto_continue_to not in self.story:
                raise GameEngineError(
                    f"Story is misconfigured: unknown auto-continue target '{scene.auto_continue_to}'."
                )

            # Auto transitions are recorded as implicit path steps.
            self.state.path.append(
                {
                    "scene_id": scene.id,
                    "scene_title": scene.title,
                    "choice_id": "auto_continue",
                    "choice_label": "Continue",
                }
            )
            self.state.current_scene = scene.auto_continue_to

    def _progress_metrics(self) -> dict[str, Any]:
        """Compute lightweight progress counters for frontend HUD."""
        total_endings = len(
            [scene for scene in self.story.values() if scene.ending and scene.ending.get("id")]
        )
        return {
            "steps": len(self.state.path),
            "chapters": len(self.state.chapters_seen),
            "endings_unlocked": len(self.state.endings_seen),
            "total_endings": total_endings,
            "completion_ratio": round(
                len(self.state.endings_seen) / total_endings if total_endings else 0.0,
                3,
            ),
        }

    def _validate_story_integrity(self) -> None:
        """Run static consistency checks on scene graph.

        This prevents runtime 500 errors from typos in scene IDs.
        """
        for scene in self.story.values():
            if scene.auto_continue_to and scene.auto_continue_to not in self.story:
                raise GameEngineError(
                    f"Scene '{scene.id}' has unknown auto_continue_to '{scene.auto_continue_to}'."
                )
            for choice in scene.choices:
                if choice.next_scene not in self.story:
                    raise GameEngineError(
                        f"Scene '{scene.id}' choice '{choice.id}' points to unknown scene '{choice.next_scene}'."
                    )
