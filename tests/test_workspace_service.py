from pathlib import Path

from forge.workspace.models import WorkspaceState
from forge.workspace.port import WorkspacePort
from forge.workspace.service import WorkspaceService


class FakeWorkspacePort(WorkspacePort):

    def state(self) -> WorkspaceState:
        return WorkspaceState(
            root=Path("."),
            file_count=10,
            python_files=4,
            exists=True,
        )

    def read_text(self, path: Path) -> str:
        return "hello"

    def write_text(self, path: Path, text: str) -> None:
        pass

    def exists(self, path: Path) -> bool:
        return True

    def list_files(self):
        return ()


def test_workspace_state():
    service = WorkspaceService(FakeWorkspacePort())

    assert service.state().exists


def test_workspace_read():
    service = WorkspaceService(FakeWorkspacePort())

    assert service.read(Path("a.txt")) == "hello"