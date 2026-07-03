from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ErrorInfo:
    """Structured information describing an error."""

    code: str
    message: str
    hint: str = ""


class ForgeError(Exception):
    """Base exception for all Forge errors."""

    def __init__(self, error: ErrorInfo):
        self.error = error
        super().__init__(error.message)

    @property
    def code(self) -> str:
        return self.error.code

    @property
    def message(self) -> str:
        return self.error.message

    @property
    def hint(self) -> str:
        return self.error.hint

    def __str__(self) -> str:
        return f"[{self.code}] {self.message}"