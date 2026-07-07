from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Import:
    """Represents a Python import statement."""

    module: Path
    target: str
    line: int