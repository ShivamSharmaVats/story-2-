"""Data models used by the game engine."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Choice:
    """A single selectable player option from a scene."""

    id: str
    label: str
    next_scene: str
    note: str = ""
    conditions: dict[str, Any] = field(default_factory=dict)
    effects: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class Scene:
    """A narrative unit with text and available choices."""

    id: str
    title: str
    chapter: str
    text: list[str]
    choices: list[Choice] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    ending: dict[str, Any] | None = None
    auto_continue_to: str | None = None


@dataclass(slots=True)
class GameState:
    """Mutable state for current player run."""

    current_scene: str | None = None
    started: bool = False
    inventory: dict[str, int] = field(default_factory=dict)
    flags: dict[str, Any] = field(default_factory=dict)
    path: list[dict[str, str]] = field(default_factory=list)
    endings_seen: list[str] = field(default_factory=list)
    chapters_seen: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Serialize state into JSON-compatible structure."""
        return {
            "current_scene": self.current_scene,
            "started": self.started,
            "inventory": self.inventory,
            "flags": self.flags,
            "path": self.path,
            "endings_seen": self.endings_seen,
            "chapters_seen": self.chapters_seen,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GameState":
        """Deserialize state safely from JSON-compatible structure."""
        return cls(
            current_scene=data.get("current_scene"),
            started=bool(data.get("started", False)),
            inventory=dict(data.get("inventory", {})),
            flags=dict(data.get("flags", {})),
            path=list(data.get("path", [])),
            endings_seen=list(data.get("endings_seen", [])),
            chapters_seen=list(data.get("chapters_seen", [])),
        )
