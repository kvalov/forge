from __future__ import annotations

from forge.analysis.models import ProjectInfo
from forge.analysis.port import AnalysisPort


class AnalysisService:
    """Business logic for project analysis."""

    def __init__(self, port: AnalysisPort):
        self._port = port

    def analyze(self) -> ProjectInfo:
        return self._port.analyze()