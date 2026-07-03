from forge.errors.base import ErrorInfo, ForgeError


class ConfigurationError(ForgeError):
    """Configuration exception."""

    def __init__(
        self,
        message: str,
        *,
        code: str = "CONFIG001",
        hint: str = "Verify Forge configuration.",
    ) -> None:
        super().__init__(
            ErrorInfo(
                code=code,
                message=message,
                hint=hint,
            )
        )