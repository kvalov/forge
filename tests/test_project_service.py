from pathlib import Path

from forge.project.models import ProjectAnalysis, ProjectInfo
from forge.project.service import ProjectService


class FakeProjectScanner:
    def scan(self) -> ProjectInfo:
        return ProjectInfo(
            root=Path("."),
            name="forge",
            total_files=3,
            python_files=3,
            test_files=1,
            has_git=True,
            has_pyproject=True,
            has_readme=True,
        )


class FakeProjectAnalyzer:
    def analyze(self, project: ProjectInfo) -> ProjectAnalysis:
        return ProjectAnalysis(
            project=project,
            modules=3,
            classes=2,
            functions=5,
            imports=4,
        )


def test_project_info() -> None:
    service = ProjectService(
        scanner=FakeProjectScanner(),
        analyzer=FakeProjectAnalyzer(),
    )

    info = service.info()

    assert info.name == "forge"
    assert info.total_files == 3
    assert info.python_files == 3
    assert info.test_files == 1


def test_project_analyze() -> None:
    service = ProjectService(
        scanner=FakeProjectScanner(),
        analyzer=FakeProjectAnalyzer(),
    )

    analysis = service.analyze()

    assert analysis.project.name == "forge"
    assert analysis.modules == 3
    assert analysis.classes == 2
    assert analysis.functions == 5
    assert analysis.imports == 4