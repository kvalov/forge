from pathlib import Path

from forge.python.builder import SymbolBuilder
from forge.python.models import (
    ClassInfo,
    FunctionInfo,
    ModuleInfo,
)


def test_build_symbol_index() -> None:
    module = ModuleInfo(
        path=Path("example.py"),
        classes=(
            ClassInfo("RepositoryService"),
        ),
        functions=(
            FunctionInfo("configure_logging"),
        ),
        imports=(),
    )

    index = SymbolBuilder().build((module,))

    assert len(index) == 2

    assert index.contains("RepositoryService")
    assert index.contains("configure_logging")