from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Branch:
    """Represents a repository branch."""

    name: str
    is_default: bool = False


@dataclass(frozen=True, slots=True)
class RepositoryState:
    """Represents the current repository state."""

    repository: str

    branch: Branch

    clean: bool

    ahead: int

    behind: int

    modified_files: tuple[Path, ...]

    staged_files: tuple[Path, ...]

    untracked_files: tuple[Path, ...]

    has_conflicts: bool

    detached_head: bool

    remote_available: bool