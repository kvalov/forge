from dataclasses import dataclass


@dataclass(slots=True)
class GitStatus:
    """Repository status."""

    repository: str

    branch: str

    dirty: bool

    modified: int

    untracked: int