from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Reference:
    """Reference to a symbol."""

    module: Path

    symbol: str

    line: int