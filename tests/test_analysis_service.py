from pathlib import Path

from forge.analysis.models import ProjectInfo
from forge.analysis.port import AnalysisPort
from forge.analysis.service import AnalysisService


class FakeAnalysisPort(AnalysisPort):
    def analyze(self) -> ProjectInfo:
        return ProjectInfo(
            root=Path("."),
            name="forge",
            packages=3,
            modules=15,
            python_files=42,
            test_files=12,
            has_pyproject=True,
            has_readme=True,
        )


def test_analysis():
    service = AnalysisService(FakeAnalysisPort())

    info = service.analyze()

    assert info.name == "forge"
    assert info.python_files == 42