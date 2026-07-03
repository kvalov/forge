from forge.models.git import GitStatus


def test_git_status():
    status = GitStatus(
        repository="forge",
        branch="main",
        dirty=False,
        modified=0,
        untracked=0,
    )

    assert status.repository == "forge"
    assert status.branch == "main"
    assert status.dirty is False