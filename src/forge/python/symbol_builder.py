from __future__ import annotations

from pathlib import Path

from forge.python.index import SymbolIndex
from forge.python.models import ModuleInfo
from forge.python.symbols import Symbol, SymbolKind


class SymbolBuilder:
    """Build a symbol index from parsed Python modules."""

    def build(
        self,
        modules: tuple[ModuleInfo, ...],
    ) -> SymbolIndex:
        index = SymbolIndex()

        for module in modules:
            self._add_module(index, module)

        return index

    def _add_module(
        self,
        index: SymbolIndex,
        module: ModuleInfo,
    ) -> None:

        relative = Path(module.path)

        for cls in module.classes:
            index.add(
                Symbol(
                    name=cls.name,
                    kind=SymbolKind.CLASS,
                    module=relative,
                    line=0,
                )
            )

        for function in module.functions:
            index.add(
                Symbol(
                    name=function.name,
                    kind=SymbolKind.FUNCTION,
                    module=relative,
                    line=0,
                )
            )