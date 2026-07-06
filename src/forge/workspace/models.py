from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class WorkspaceFile:
    """Represents a file inside the workspace."""

    path: Path
    size: int


@dataclass(frozen=True, slots=True)
class WorkspaceState:
    """Represents the current workspace."""

    root: Path

    project_name: str

    exists: bool

    file_count: int

    directory_count: int

    python_files: int

    has_git: bool

    has_pyproject: bool

    has_readme: bool

    has_tests: bool