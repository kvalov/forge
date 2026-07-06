from __future__ import annotations

from typing import Protocol

from forge.project.models import ProjectInfo


class ProjectPort(Protocol):
    """Project discovery abstraction."""

    def scan(self) -> ProjectInfo:
        """Scan the current project."""
        ...