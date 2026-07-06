from __future__ import annotations

from pathlib import Path

IGNORED_DIRECTORIES = frozenset(
    {
        ".git",
        ".venv",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
        ".idea",
        ".vscode",
        "node_modules",
        "build",
        "dist",
        ".tox",
        ".coverage",
    }
)

IGNORED_FILES = frozenset(
    {
        ".DS_Store",
        "Thumbs.db",
    }
)


def is_ignored(path: Path) -> bool:
    """Return True if the path should be ignored."""

    if path.name in IGNORED_FILES:
        return True

    return any(
        part in IGNORED_DIRECTORIES
        for part in path.parts
    )