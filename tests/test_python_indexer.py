from pathlib import Path

from forge.infrastructure.filesystem.local_filesystem_adapter import (
    LocalFilesystemAdapter,
)
from forge.python.indexer import PythonIndexer
from forge.workspace.service import WorkspaceService


def test_python_indexer(tmp_path: Path) -> None:
    source = tmp_path / "example.py"

    source.write_text(
        """
class Demo:
    pass

def hello():
    pass
""",
        encoding="utf-8",
    )

    workspace = WorkspaceService(
        LocalFilesystemAdapter(tmp_path)
    )

    index = PythonIndexer(workspace).build()

    assert len(index) == 2
    assert index.contains("Demo")
    assert index.contains("hello")