from typing import Callable, Any

# Stores every registered skill
_SKILLS: dict[str, Callable[..., Any]] = {}


def register(name: str, handler: Callable[..., Any]) -> None:
    """Register a skill."""
    _SKILLS[name.lower()] = handler


def get(name: str):
    """Return a registered skill."""
    return _SKILLS.get(name.lower())


def all_skills():
    """Return all registered skills."""
    return _SKILLS