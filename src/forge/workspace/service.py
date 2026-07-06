from __future__ import annotations

from pathlib import Path

from forge.workspace.models import WorkspaceFile, WorkspaceState
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

    def files(self) -> tuple[WorkspaceFile, ...]:
        """Return all files in the workspace."""
        return self._port.list_files()

    def python_files(self) -> tuple[WorkspaceFile, ...]:
        """Return all Python source files."""
        return tuple(
            file
            for file in self.files()
            if file.path.suffix == ".py"
        )

    def test_files(self) -> tuple[WorkspaceFile, ...]:
        """Return all Python test files."""
        return tuple(
            file
            for file in self.python_files()
            if (
                file.path.name.startswith("test_")
                or "tests" in file.path.parts
            )
        )