from __future__ import annotations

from pathlib import Path
from typing import Protocol

from forge.workspace.models import WorkspaceFile, WorkspaceState


class WorkspacePort(Protocol):
    """Workspace abstraction."""

    def state(self) -> WorkspaceState:
        ...

    def exists(self, path: Path) -> bool:
        ...

    def read_text(self, path: Path) -> str:
        ...

    def write_text(self, path: Path, text: str) -> None:
        ...

    def mkdir(self, path: Path) -> None:
        ...

    def delete(self, path: Path) -> None:
        ...

    def move(self, source: Path, destination: Path) -> None:
        ...

    def list_files(self) -> tuple[WorkspaceFile, ...]:
        ...