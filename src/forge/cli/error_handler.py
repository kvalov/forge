import typer

from forge.errors import ForgeError
from forge.logging.logger import get_logger

logger = get_logger(__name__)


def handle_error(error: ForgeError) -> "typer.Exit":
    """Handle a ForgeError consistently."""

    logger.error(
        "Forge error",
        code=error.code,
        message=error.message,
    )

    typer.secho(
        f"\nERROR {error.code}",
        fg=typer.colors.RED,
        bold=True,
    )

    typer.echo()
    typer.echo(error.message)

    if error.hint:
        typer.echo()
        typer.secho("Hint:", fg=typer.colors.YELLOW)
        typer.echo(error.hint)

    return typer.Exit(code=1)