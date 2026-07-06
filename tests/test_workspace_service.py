from pathlib import Path

from forge.workspace.models import WorkspaceState
from forge.workspace.port import WorkspacePort
from forge.workspace.service import WorkspaceService


class FakeWorkspacePort(WorkspacePort):
    def state(self) -> WorkspaceState:
        return WorkspaceState(
            root=Path("."),
            project_name="forge",
            exists=True,
            file_count=10,
            directory_count=2,
            python_files=4,
            has_git=True,
            has_pyproject=True,
            has_readme=True,
            has_tests=True,
        )

    def read_text(self, path: Path) -> str:
        return "hello"

    def write_text(self, path: Path, text: str) -> None:
        pass

    def exists(self, path: Path) -> bool:
        return True

    def mkdir(self, path: Path) -> None:
        pass

    def delete(self, path: Path) -> None:
        pass

    def move(self, source: Path, destination: Path) -> None:
        pass

    def list_files(self):
        return ()


def test_workspace_state():
    service = WorkspaceService(FakeWorkspacePort())

    state = service.state()

    assert state.exists
    assert state.project_name == "forge"
    assert state.python_files == 4


def test_workspace_read():
    service = WorkspaceService(FakeWorkspacePort())

    assert service.read(Path("a.txt")) == "hello"


def test_workspace_exists():
    service = WorkspaceService(FakeWorkspacePort())

    assert service.exists(Path("anything")) is True