from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class GitStatus:
    """Repository status information."""

    repository: str
    branch: str
    dirty: bool
    modified: int
    untracked: int