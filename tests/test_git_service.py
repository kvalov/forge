from forge.models.git import GitStatus
from forge.services.git import GitService


class FakeGitProvider:
    def status(self) -> GitStatus:
        return GitStatus(
            repository="forge",
            branch="main",
            dirty=False,
            modified=0,
            untracked=0,
        )


def test_git_service_status():
    service = GitService(FakeGitProvider())

    status = service.status()

    assert status.repository == "forge"
    assert status.branch == "main"
    assert status.dirty is False