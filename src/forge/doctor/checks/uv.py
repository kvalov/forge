from __future__ import annotations

import shutil

from forge.doctor.checks.base import DoctorCheck
from forge.doctor.models import CheckResult


class UvCheck(DoctorCheck):

    @property
    def name(self) -> str:
        return "uv"

    def run(self) -> CheckResult:
        path = shutil.which("uv")

        return CheckResult(
            name=self.name,
            ok=path is not None,
            message=path or "uv not found",
        )