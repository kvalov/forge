from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Forge configuration."""

    workspace: Path = Path.cwd()

    log_level: str = "INFO"

    log_file: Path = Path("logs/forge.log")

    model_config = SettingsConfigDict(
        env_prefix="FORGE_",
        case_sensitive=False,
    )


settings = Settings()