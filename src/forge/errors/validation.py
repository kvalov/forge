from forge.errors.base import ErrorInfo, ForgeError


class ValidationError(ForgeError):
    def __init__(
        self,
        message: str,
        hint: str = "Verify the provided input.",
    ):
        super().__init__(
            ErrorInfo(
                code="VALID001",
                message=message,
                hint=hint,
            )
        )