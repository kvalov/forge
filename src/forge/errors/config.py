from forge.errors.base import ErrorInfo, ForgeError


class ConfigurationError(ForgeError):
    def __init__(
        self,
        message: str,
        hint: str = "Verify your Forge configuration.",
    ):
        super().__init__(
            ErrorInfo(
                code="CONFIG001",
                message=message,
                hint=hint,
            )
        )