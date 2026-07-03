import platform
import shutil
import subprocess
import sys
from pathlib import Path

from forge.logging.logger import configure_logging, logger


def check() -> int:
    """Run environment diagnostics."""

    configure_logging()
    logger.info("Running doctor")

    print("Forge Doctor v0.1")
    print("-" * 50)

    # Python
    print(f"Python       : {platform.python_version()}")

    # Git
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

    # uv
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

    # Virtual environment
    venv_ok = sys.prefix != sys.base_prefix
    print(f"Virtual Env  : {'YES' if venv_ok else 'NO'}")

    # Workspace
    cwd = Path.cwd()
    print(f"Workspace    : {cwd}")

    # Project
    project_ok = (cwd / "pyproject.toml").exists()
    project_name = cwd.name if project_ok else "UNKNOWN"

    print(f"Project      : {project_name}")

    # PATH
    git_path = shutil.which("git")
    print(f"Git PATH     : {git_path if git_path else 'NOT FOUND'}")

    print("-" * 50)

    healthy = (
        git_ok
        and uv_ok
        and venv_ok
        and project_ok
    )

    print(f"Status       : {'HEALTHY' if healthy else 'WARNING'}")

    return 0 if healthy else 1