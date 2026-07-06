from __future__ import annotations

import ast
from pathlib import Path

from forge.python.models import ModuleInfo
from forge.python.visitor import ModuleVisitor


class PythonParser:
    """Parse Python source files."""

    def parse(
        self,
        path: Path,
    ) -> ModuleInfo:

        source = path.read_text(
            encoding="utf-8"
        )

        tree = ast.parse(
            source,
            filename=str(path),
        )

        visitor = ModuleVisitor()

        visitor.visit(tree)

        return ModuleInfo(
            path=path,
            classes=tuple(visitor.classes),
            functions=tuple(visitor.functions),
            imports=tuple(visitor.imports),
        )