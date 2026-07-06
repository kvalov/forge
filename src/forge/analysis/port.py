from __future__ import annotations

from typing import Protocol

from forge.analysis.models import ProjectInfo


class AnalysisPort(Protocol):
    """Project analysis abstraction."""

    def analyze(self) -> ProjectInfo:
        ...