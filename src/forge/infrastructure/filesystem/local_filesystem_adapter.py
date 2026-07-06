from __future__ import annotations

from pathlib import Path

from forge.workspace.models import WorkspaceFile, WorkspaceState
from forge.workspace.port import WorkspacePort


class LocalFilesystemAdapter(WorkspacePort):
    """Local filesystem implementation."""

    def __init__(self, root: Path | None = None) -> None:
        self._root = root or Path.cwd()

    def state(self) -> WorkspaceState:
        files = [p for p in self._root.rglob("*") if p.is_file()]
        directories = [p for p in self._root.rglob("*") if p.is_dir()]

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
        return (self._root / path).exists()

    def read_text(self, path: Path) -> str:
        return (self._root / path).read_text(encoding="utf-8")

    def write_text(self, path: Path, text: str) -> None:
        target = self._root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    def mkdir(self, path: Path) -> None:
        (self._root / path).mkdir(parents=True, exist_ok=True)

    def delete(self, path: Path) -> None:
        target = self._root / path
        if target.exists():
            target.unlink()

    def move(self, source: Path, destination: Path) -> None:
        (self._root / source).rename(self._root / destination)

    def list_files(self) -> tuple[WorkspaceFile, ...]:
        files: list[WorkspaceFile] = []

        for file in self._root.rglob("*"):
            if file.is_file():
                files.append(
                    WorkspaceFile(
                        path=file.relative_to(self._root),
                        size=file.stat().st_size,
                    )
                )

        return tuple(files)