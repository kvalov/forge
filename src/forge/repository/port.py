from __future__ import annotations

from typing import Protocol

from forge.repository.models import RepositoryState


class RepositoryPort(Protocol):
    """Contract for repository operations."""

    def state(self) -> RepositoryState:
        """Return current repository state."""
        ...

    def fetch(self) -> None:
        """Fetch remote changes."""
        ...

    def pull(self) -> None:
        """Pull remote changes."""
        ...

    def push(self) -> None:
        """Push local changes."""
        ...

    def commit(self, message: str) -> None:
        """Create a commit."""
        ...

    def checkout(self, branch: str) -> None:
        """Switch branch."""
        ...

    def create_branch(self, branch: str) -> None:
        """Create a branch."""
        ...