from pathlib import Path

from forge.repository.models import Branch, RepositoryState


def test_repository_state():
    state = RepositoryState(
        repository="forge",
        branch=Branch(
            name="main",
            is_default=True,
        ),
        clean=True,
        ahead=0,
        behind=0,
        modified_files=(),
        staged_files=(),
        untracked_files=(Path("README.md"),),
        has_conflicts=False,
        detached_head=False,
        remote_available=True,
    )

    assert state.repository == "forge"
    assert state.branch.name == "main"
    assert state.clean