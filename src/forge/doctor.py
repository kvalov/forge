from __future__ import annotations

import platform
import shutil
import sys
from pathlib import Path


def check() -> int:
    print("Forge Doctor v0.1")
    print("-" * 40)

    # Python
    print(f"Python       : {platform.python_version()}")

    # Git
    git_ok = shutil.which("git") is not None
    print(f"Git          : {'OK' if git_ok else 'NOT FOUND'}")

    # uv
    uv_ok = shutil.which("uv") is not None
    print(f"uv           : {'OK' if uv_ok else 'NOT FOUND'}")

    # Virtual environment
    venv = sys.prefix != sys.base_prefix
    print(f"Virtual Env  : {'YES' if venv else 'NO'}")

    # Workspace
    cwd = Path.cwd()
    print(f"Workspace    : {cwd}")

    # Project
    project_ok = (cwd / "pyproject.toml").exists()
    print(f"Project      : {'OK' if project_ok else 'NOT FOUND'}")

    healthy = git_ok and project_ok and venv

    print("-" * 40)
    print(f"Status       : {'HEALTHY' if healthy else 'WARNING'}")

    return 0 if healthy else 1