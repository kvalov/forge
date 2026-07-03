from pathlib import Path

from git import InvalidGitRepositoryError, NoSuchPathError, Repo

from forge.errors import GitError
from forge.models.git import GitStatus
from forge.providers.git import GitProvider


class GitPythonProvider(GitProvider):
    """Git provider backed by GitPython."""

    def __init__(self, path: Path | None = None):
        self._path = path or Path.cwd()

    def status(self) -> GitStatus:
        try:
            repo = Repo(str(self._path))

        except (InvalidGitRepositoryError, NoSuchPathError) as exc:
            raise GitError(
                "Current directory is not a Git repository."
            ) from exc

        return GitStatus(
            repository=Path(repo.working_dir).name,
            branch=repo.active_branch.name,
            dirty=repo.is_dirty(),
            modified=len(repo.index.diff(None)),
            untracked=len(repo.untracked_files),
        )