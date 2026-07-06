from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class ClassInfo:
    name: str


@dataclass(frozen=True, slots=True)
class FunctionInfo:
    name: str


@dataclass(frozen=True, slots=True)
class ImportInfo:
    module: str


@dataclass(frozen=True, slots=True)
class ModuleInfo:
    """Parsed Python module."""

    path: Path

    classes: tuple[ClassInfo, ...]

    functions: tuple[FunctionInfo, ...]

    imports: tuple[ImportInfo, ...]

@dataclass(frozen=True, slots=True)
class ModuleAnalysis:
    """High-level analysis of a Python module."""

    module: ModuleInfo

    class_count: int

    function_count: int

    import_count: int