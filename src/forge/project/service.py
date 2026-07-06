from __future__ import annotations

from forge.project.analyzer import ProjectAnalyzer
from forge.project.models import ProjectAnalysis, ProjectInfo
from forge.project.scanner import ProjectScanner


class ProjectService:
    """Project business service."""

    def __init__(
        self,
        scanner: ProjectScanner,
        analyzer: ProjectAnalyzer,
    ) -> None:
        self._scanner = scanner
        self._analyzer = analyzer

    def info(self) -> ProjectInfo:
        return self._scanner.scan()

    def analyze(self) -> ProjectAnalysis:
        project = self.info()
        return self._analyzer.analyze(project)