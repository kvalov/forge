from __future__ import annotations

from forge.project.models import ProjectInfo
from forge.workspace.service import WorkspaceService


class ProjectScanner:
    """Scans the current workspace."""

    def __init__(self, workspace: WorkspaceService):
        self._workspace = workspace

    def scan(self) -> ProjectInfo:
        workspace = self._workspace.state()

        files = self._workspace.files()
        python_files = self._workspace.python_files()
        test_files = self._workspace.test_files()

        return ProjectInfo(
            root=workspace.root,
            name=workspace.project_name,
            total_files=len(files),
            python_files=len(python_files),
            test_files=len(test_files),
            has_git=workspace.has_git,
            has_pyproject=workspace.has_pyproject,
            has_readme=workspace.has_readme,
        )