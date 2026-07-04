from __future__ import annotations

from forge.repository.models import RepositoryState
from forge.repository.port import RepositoryPort


class RepositoryService:
    """Business logic for repository operations."""

    def __init__(self, port: RepositoryPort):
        self._port = port

    def state(self) -> RepositoryState:
        """Return the current repository state."""
        return self._port.state()

    def is_clean(self) -> bool:
        """Return True if the repository has no local changes."""
        return self.state().clean

    def has_remote(self) -> bool:
        """Return True if a remote repository is configured."""
        return self.state().remote_available

    def can_publish(self) -> bool:
        """Return True if publishing is currently possible."""
        state = self.state()

        return (
            state.remote_available
            and not state.has_conflicts
            and not state.detached_head
        )

    def prepare_workspace(self) -> RepositoryState:
        """
        Validate that the repository is ready for work.

        Future versions will:
        - fetch()
        - verify default branch
        - verify clean state
        - verify remote

        For now it only returns the current state.
        """
        return self.state()