from pathlib import Path

from forge.infrastructure.filesystem.local_filesystem_adapter import (
    LocalFilesystemAdapter,
)


def test_workspace_exists(tmp_path: Path):
    adapter = LocalFilesystemAdapter(tmp_path)

    assert adapter.state().exists