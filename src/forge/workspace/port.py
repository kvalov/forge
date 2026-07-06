from __future__ import annotations

from pathlib import Path
from typing import Protocol

from forge.workspace.models import WorkspaceFile, WorkspaceState


class WorkspacePort(Protocol):
    """Workspace abstraction."""

    def state(self) -> WorkspaceState:
        ...

    def read_text(self, path: Path) -> str:
        ...

    def write_text(self, path: Path, text: str) -> None:
        ...

    def exists(self, path: Path) -> bool:
        ...

    def list_files(self) -> tuple[WorkspaceFile, ...]:
        ...