from pathlib import Path

from forge.infrastructure.filesystem.local_filesystem_adapter import (
    LocalFilesystemAdapter,
)
from forge.project.analyzer import ProjectAnalyzer
from forge.project.scanner import ProjectScanner
from forge.project.service import ProjectService
from forge.workspace.service import WorkspaceService


def test_project_analysis(tmp_path: Path):
    source = tmp_path / "main.py"

    source.write_text(
        """
import pathlib

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

    scanner = ProjectScanner(workspace)

    analyzer = ProjectAnalyzer(workspace)

    service = ProjectService(
        scanner,
        analyzer,
    )

    analysis = service.analyze()

    assert analysis.modules == 1
    assert analysis.classes == 1
    assert analysis.functions == 1
    assert analysis.imports == 1