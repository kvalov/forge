from __future__ import annotations

from pathlib import Path

from forge.doctor.checks.base import DoctorCheck
from forge.doctor.models import CheckResult


class WorkspaceCheck(DoctorCheck):

    @property
    def name(self) -> str:
        return "Workspace"

    def run(self) -> CheckResult:
        root = Path.cwd()

        return CheckResult(
            name=self.name,
            ok=(root / "pyproject.toml").exists(),
            message=str(root),
        )