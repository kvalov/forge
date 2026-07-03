from typing import Protocol

from forge.models.git import GitStatus


class GitProvider(Protocol):
    """Git provider interface."""

    def status(self) -> GitStatus:
        """Return repository status."""
        ...