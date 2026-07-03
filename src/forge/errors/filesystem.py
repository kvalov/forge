from forge.errors.base import ErrorInfo, ForgeError


class FilesystemError(ForgeError):
    """Filesystem exception."""

    def __init__(
        self,
        message: str,
        *,
        code: str = "FS001",
        hint: str = "Verify filesystem path.",
    ) -> None:
        super().__init__(
            ErrorInfo(
                code=code,
                message=message,
                hint=hint,
            )
        )