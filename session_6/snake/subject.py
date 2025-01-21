# ruff: noqa: D100,S311

# First party
import logging

from .observer import Observer

logger = logging.getLogger("foo")
class Subject:
    """Mother class representing a subject for the Observer pattern."""

    def __init__(self) -> None:
        """Object initialization."""
        super().__init__()
        self._observers: list[Observer] = []

    @property
    def observers(self) -> list[Observer]:
        """List of observers."""
        return self._observers

    def attach_obs(self, obs: Observer) -> None:
        """Attach an observer."""
        logger.info("Attach an observer")
        self._observers.append(obs)

    def detach_obs(self, obs: Observer) -> None:
        """Detach an observer."""
        logger.info("Detach an observer")
        self._observers.remove(obs)
