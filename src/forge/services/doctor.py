from __future__ import annotations

import platform
import shutil
import subprocess
import sys
from pathlib import Path

from forge.doctor.checks.git import GitCheck
from forge.doctor.checks.python import PythonCheck
from forge.doctor.checks.uv import UvCheck
from forge.doctor.checks.workspace import WorkspaceCheck
from forge.doctor.runner import DoctorRunner
from forge.logging.logger import get_logger

logger = get_logger(__name__)


class DoctorService:
    """Environment diagnostics service."""

    def check(self) -> int:
        logger.info("Running doctor")

        runner = DoctorRunner()

        #
        # Execute checks
        #
        runner.add(PythonCheck().run())
        runner.add(GitCheck().run())
        runner.add(UvCheck().run())
        runner.add(WorkspaceCheck().run())

        report = runner.report()

        #
        # Additional information for display
        #
        git_version = "NOT FOUND"

        try:
            result = subprocess.run(
                ["git", "--version"],
                capture_output=True,
                text=True,
                check=True,
            )
            git_version = result.stdout.strip()

        except Exception:
            pass

        uv_version = "NOT FOUND"

        try:
            result = subprocess.run(
                ["py", "-3.12", "-m", "uv", "--version"],
                capture_output=True,
                text=True,
                check=True,
            )
            uv_version = result.stdout.strip()

        except Exception:
            pass

        cwd = Path.cwd()
        project_ok = (cwd / "pyproject.toml").exists()

        print("Forge Doctor v0.1")
        print("-" * 50)

        print(f"Python       : {platform.python_version()}")
        print(f"Git          : {git_version}")
        print(f"uv           : {uv_version}")
        print(f"Virtual Env  : {'YES' if sys.prefix != sys.base_prefix else 'NO'}")
        print(f"Workspace    : {cwd}")
        print(f"Project      : {cwd.name if project_ok else 'UNKNOWN'}")
        print(f"Git PATH     : {shutil.which('git') or 'NOT FOUND'}")

        print("-" * 50)

        logger.info(
            "Doctor completed",
            healthy=report.healthy,
        )

        print(
            f"Status       : {'HEALTHY' if report.healthy else 'WARNING'}"
        )

        return 0 if report.healthy else 1