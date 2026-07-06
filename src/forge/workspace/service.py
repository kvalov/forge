from __future__ import annotations

from pathlib import Path

from forge.workspace.models import WorkspaceState
from forge.workspace.port import WorkspacePort


class WorkspaceService:
    """Workspace business logic."""

    def __init__(self, port: WorkspacePort):
        self._port = port

    def state(self) -> WorkspaceState:
        return self._port.state()

    def exists(self, path: Path) -> bool:
        return self._port.exists(path)

    def read(self, path: Path) -> str:
        return self._port.read_text(path)

    def write(self, path: Path, text: str) -> None:
        self._port.write_text(path, text)