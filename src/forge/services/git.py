from forge.models.git import GitStatus
from forge.providers.git import GitProvider


class GitService:
    """Git business logic."""

    def __init__(self, provider: GitProvider):
        self._provider = provider

    def status(self) -> GitStatus:
        return self._provider.status()