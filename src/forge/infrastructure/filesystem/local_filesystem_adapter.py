from __future__ import annotations

from pathlib import Path

from forge.workspace.ignore import is_ignored
from forge.workspace.models import WorkspaceFile, WorkspaceState
from forge.workspace.port import WorkspacePort


class LocalFilesystemAdapter(WorkspacePort):
    """Local filesystem implementation of WorkspacePort."""

    def __init__(self, root: Path | None = None) -> None:
        self._root = root or Path.cwd()

    def _iter_files(self) -> tuple[Path, ...]:
        """Return all project files excluding ignored paths."""
        files: list[Path] = []

        for path in self._root.rglob("*"):
            if not path.is_file():
                continue

            relative = path.relative_to(self._root)

            if is_ignored(relative):
                continue

            files.append(path)

        return tuple(files)

    def _iter_directories(self) -> tuple[Path, ...]:
        """Return all project directories excluding ignored paths."""
        directories: list[Path] = []

        for path in self._root.rglob("*"):
            if not path.is_dir():
                continue

            relative = path.relative_to(self._root)

            if is_ignored(relative):
                continue

            directories.append(path)

        return tuple(directories)

    def state(self) -> WorkspaceState:
        """Return workspace information."""
        files = self._iter_files()
        directories = self._iter_directories()

        return WorkspaceState(
            root=self._root,
            project_name=self._root.name,
            exists=self._root.exists(),
            file_count=len(files),
            directory_count=len(directories),
            python_files=sum(
                1
                for file in files
                if file.suffix == ".py"
            ),
            has_git=(self._root / ".git").exists(),
            has_pyproject=(self._root / "pyproject.toml").exists(),
            has_readme=any(
                (self._root / name).exists()
                for name in (
                    "README.md",
                    "README.rst",
                    "README.txt",
                )
            ),
            has_tests=(self._root / "tests").exists(),
        )

    def exists(self, path: Path) -> bool:
        """Return True if a path exists."""
        return (self._root / path).exists()

    def read_text(self, path: Path) -> str:
        """Read a UTF-8 text file."""
        return (self._root / path).read_text(
            encoding="utf-8",
        )

    def write_text(self, path: Path, text: str) -> None:
        """Write a UTF-8 text file."""
        target = self._root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            text,
            encoding="utf-8",
        )

    def mkdir(self, path: Path) -> None:
        """Create a directory."""
        (self._root / path).mkdir(
            parents=True,
            exist_ok=True,
        )

    def delete(self, path: Path) -> None:
        """Delete a file if it exists."""
        target = self._root / path

        if target.exists():
            target.unlink()

    def move(
        self,
        source: Path,
        destination: Path,
    ) -> None:
        """Move or rename a file."""
        target = self._root / destination
        target.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        (self._root / source).rename(target)

    def list_files(self) -> tuple[WorkspaceFile, ...]:
        """Return all project files."""
        return tuple(
            WorkspaceFile(
                path=file.relative_to(self._root),
                size=file.stat().st_size,
            )
            for file in self._iter_files()
        )