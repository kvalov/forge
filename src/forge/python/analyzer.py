from __future__ import annotations

from forge.python.models import ModuleAnalysis, ModuleInfo


class ModuleAnalyzer:
    """Analyze parsed Python modules."""

    def analyze(
        self,
        module: ModuleInfo,
    ) -> ModuleAnalysis:

        return ModuleAnalysis(
            module=module,
            class_count=len(module.classes),
            function_count=len(module.functions),
            import_count=len(module.imports),
        )