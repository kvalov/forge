from __future__ import annotations

from forge.project.models import ProjectAnalysis, ProjectInfo
from forge.python.parser import PythonParser
from forge.workspace.service import WorkspaceService


class ProjectAnalyzer:
    """Analyze all Python modules in a workspace."""

    def __init__(
        self,
        workspace: WorkspaceService,
        parser: PythonParser | None = None,
    ) -> None:
        self._workspace = workspace
        self._parser = parser or PythonParser()

    def analyze(self, project: ProjectInfo) -> ProjectAnalysis:
        modules = 0
        classes = 0
        functions = 0
        imports = 0

        root = self._workspace.state().root

        for file in self._workspace.python_files():
            module = self._parser.parse(root / file.path)

            modules += 1
            classes += len(module.classes)
            functions += len(module.functions)
            imports += len(module.imports)

        return ProjectAnalysis(
            project=project,
            modules=modules,
            classes=classes,
            functions=functions,
            imports=imports,
        )