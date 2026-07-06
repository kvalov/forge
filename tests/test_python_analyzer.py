from pathlib import Path

from forge.python.analyzer import ModuleAnalyzer
from forge.python.models import (
    ClassInfo,
    FunctionInfo,
    ImportInfo,
    ModuleInfo,
)


def test_module_analyzer() -> None:
    module = ModuleInfo(
        path=Path("main.py"),
        classes=(ClassInfo("Demo"),),
        functions=(FunctionInfo("hello"),),
        imports=(ImportInfo("pathlib"),),
    )

    analysis = ModuleAnalyzer().analyze(module)

    assert analysis.class_count == 1
    assert analysis.function_count == 1
    assert analysis.import_count == 1