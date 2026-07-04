from pathlib import Path

from forge.repository.models import Branch, RepositoryState
from forge.repository.port import RepositoryPort
from forge.repository.service import RepositoryService


class FakeRepositoryPort(RepositoryPort):

    def state(self) -> RepositoryState:
        return RepositoryState(
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

    def fetch(self) -> None:
        pass

    def pull(self) -> None:
        pass

    def push(self) -> None:
        pass

    def commit(self, message: str) -> None:
        pass

    def checkout(self, branch: str) -> None:
        pass

    def create_branch(self, branch: str) -> None:
        pass


def test_repository_is_clean():
    service = RepositoryService(FakeRepositoryPort())

    assert service.is_clean()


def test_repository_has_remote():
    service = RepositoryService(FakeRepositoryPort())

    assert service.has_remote()


def test_repository_can_publish():
    service = RepositoryService(FakeRepositoryPort())

    assert service.can_publish()


def test_prepare_workspace():
    service = RepositoryService(FakeRepositoryPort())

    state = service.prepare_workspace()

    assert state.repository == "forge"