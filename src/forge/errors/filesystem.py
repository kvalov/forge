from forge.errors.base import ErrorInfo, ForgeError


class FilesystemError(ForgeError):
    def __init__(
        self,
        message: str,
        hint: str = "Verify the filesystem path.",
    ):
        super().__init__(
            ErrorInfo(
                code="FS001",
                message=message,
                hint=hint,
            )
        )