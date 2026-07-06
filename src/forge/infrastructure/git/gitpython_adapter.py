from __future__ import annotations

from pathlib import Path
from typing import Iterable

from git import InvalidGitRepositoryError, NoSuchPathError, Repo
from git.diff import Diff

from forge.errors import GitError
from forge.repository.models import Branch, RepositoryState
from forge.repository.port import RepositoryPort


class GitPythonAdapter(RepositoryPort):
    """GitPython implementation of RepositoryPort."""

    def __init__(self, path: Path | None = None) -> None:
        self._path = path or Path.cwd()

    def _repo(self) -> Repo:
        """Return the current Git repository."""
        try:
            return Repo(str(self._path))
        except (InvalidGitRepositoryError, NoSuchPathError) as exc:
            raise GitError(
                "Current directory is not a Git repository."
            ) from exc

    @staticmethod
    def _paths(diffs: Iterable[Diff]) -> tuple[Path, ...]:
        """Convert GitPython Diff objects to Path objects."""
        return tuple(
            Path(diff.a_path)
            for diff in diffs
            if diff.a_path is not None
        )

    def state(self) -> RepositoryState:
        """Return the current repository state."""
        repo = self._repo()

        working_tree = repo.working_tree_dir
        if working_tree is None:
            raise GitError("Repository has no working tree.")

        if repo.head.is_detached:
            branch = Branch(
                name="HEAD",
                is_default=False,
            )
        else:
            branch = Branch(
                name=repo.active_branch.name,
                is_default=repo.active_branch.name == "main",
            )

        return RepositoryState(
            repository=Path(working_tree).name,
            branch=branch,
            clean=not repo.is_dirty(untracked_files=True),
            ahead=0,
            behind=0,
            modified_files=self._paths(repo.index.diff(None)),
            staged_files=self._paths(repo.index.diff("HEAD")),
            untracked_files=tuple(
                Path(path)
                for path in repo.untracked_files
            ),
            has_conflicts=False,
            detached_head=repo.head.is_detached,
            remote_available=bool(repo.remotes),
        )

    def fetch(self) -> None:
        """Fetch changes from all remotes."""
        for remote in self._repo().remotes:
            remote.fetch()

    def pull(self) -> None:
        """Pull changes from origin."""
        self._repo().remotes.origin.pull()

    def push(self) -> None:
        """Push changes to origin."""
        self._repo().remotes.origin.push()

    def commit(self, message: str) -> None:
        """Create a commit."""
        repo = self._repo()
        repo.git.add(A=True)
        repo.index.commit(message)

    def checkout(self, branch: str) -> None:
        """Checkout an existing branch."""
        self._repo().git.checkout(branch)

    def create_branch(self, branch: str) -> None:
        """Create and checkout a new branch."""
        self._repo().git.checkout("-b", branch)