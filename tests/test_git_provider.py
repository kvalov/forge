from forge.infrastructure.git import GitPythonProvider


def test_provider_creation():
    provider = GitPythonProvider()

    assert provider is not None