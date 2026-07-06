from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class ProjectInfo:
    """High-level information about a software project."""

    root: Path

    name: str

    packages: int

    modules: int

    python_files: int

    test_files: int

    has_pyproject: bool

    has_readme: bool