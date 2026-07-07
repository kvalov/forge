from __future__ import annotations

import shutil

from forge.doctor.checks.base import DoctorCheck
from forge.doctor.models import CheckResult


class GitCheck(DoctorCheck):

    @property
    def name(self) -> str:
        return "Git"

    def run(self) -> CheckResult:
        path = shutil.which("git")

        return CheckResult(
            name=self.name,
            ok=path is not None,
            message=path or "Git not found",
        )