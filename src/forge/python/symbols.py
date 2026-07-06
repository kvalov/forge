from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class SymbolKind(str, Enum):
    """Supported symbol types."""

    CLASS = "class"
    FUNCTION = "function"
    METHOD = "method"


@dataclass(frozen=True, slots=True)
class Symbol:
    """Represents a Python symbol."""

    name: str

    kind: SymbolKind

    module: Path

    line: int