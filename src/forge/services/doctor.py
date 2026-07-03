from __future__ import annotations

import platform
import shutil
import subprocess
import sys
from pathlib import Path

from forge.logging.logger import get_logger

logger = get_logger(__name__)


class DoctorService:
    """Environment diagnostics service."""

    def check(self) -> int:
        logger.info("Running doctor")

        print("Forge Doctor v0.1")
        print("-" * 50)

        print(f"Python       : {platform.python_version()}")

        git_version = "NOT FOUND"
        git_ok = False

        try:
            result = subprocess.run(
                ["git", "--version"],
                capture_output=True,
                text=True,
                check=True,
            )
            git_version = result.stdout.strip()
            git_ok = True
        except Exception:
            pass

        print(f"Git          : {git_version}")

        uv_version = "NOT FOUND"
        uv_ok = False

        try:
            result = subprocess.run(
                ["py", "-3.12", "-m", "uv", "--version"],
                capture_output=True,
                text=True,
                check=True,
            )
            uv_version = result.stdout.strip()
            uv_ok = True
        except Exception:
            pass

        print(f"uv           : {uv_version}")

        venv_ok = sys.prefix != sys.base_prefix
        print(f"Virtual Env  : {'YES' if venv_ok else 'NO'}")

        cwd = Path.cwd()
        print(f"Workspace    : {cwd}")

        project_ok = (cwd / "pyproject.toml").exists()
        print(f"Project      : {cwd.name if project_ok else 'UNKNOWN'}")

        print(f"Git PATH     : {shutil.which('git') or 'NOT FOUND'}")

        print("-" * 50)

        healthy = git_ok and uv_ok and venv_ok and project_ok

        logger.info("Doctor completed", healthy=healthy)

        print(f"Status       : {'HEALTHY' if healthy else 'WARNING'}")

        return 0 if healthy else 1