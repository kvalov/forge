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

    file_count: int

    python_files: int

    exists: bool