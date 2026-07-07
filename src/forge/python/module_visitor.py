from __future__ import annotations

import ast


from forge.python.models import (
    ClassInfo,
    FunctionInfo,
    ImportInfo,
)


class ModuleVisitor(ast.NodeVisitor):
    """Collect high-level information from a Python module."""

    def __init__(self) -> None:
        self.classes: list[ClassInfo] = []
        self.functions: list[FunctionInfo] = []
        self.imports: list[ImportInfo] = []

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self.classes.append(
            ClassInfo(node.name)
        )

        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.functions.append(
            FunctionInfo(node.name)
        )

        self.generic_visit(node)

    def visit_AsyncFunctionDef(
        self,
        node: ast.AsyncFunctionDef,
    ) -> None:
        self.functions.append(
            FunctionInfo(node.name)
        )

        self.generic_visit(node)

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            self.imports.append(
                ImportInfo(alias.name)
            )

    def visit_ImportFrom(
        self,
        node: ast.ImportFrom,
    ) -> None:
        if node.module:
            self.imports.append(
                ImportInfo(node.module)
            )