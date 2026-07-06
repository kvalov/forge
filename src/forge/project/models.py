from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class ProjectInfo:
    root: Path
    name: str

    total_files: int
    python_files: int
    test_files: int

    has_git: bool
    has_pyproject: bool
    has_readme: bool


@dataclass(frozen=True, slots=True)
class ProjectAnalysis:
    """High-level project analysis."""

    project: ProjectInfo

    modules: int

    classes: int

    functions: int

    imports: int