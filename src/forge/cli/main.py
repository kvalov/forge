import typer

from forge.cli.error_handler import handle_error
from forge.errors import ForgeError
from forge.services.doctor import check

app = typer.Typer(
    help="Forge AI Software Engineer",
)


@app.callback()
def callback() -> None:
    """Forge CLI."""


@app.command()
def doctor() -> None:
    """Run environment diagnostics."""

    try:
        raise typer.Exit(check())

    except ForgeError as error:
        raise handle_error(error)


def main() -> None:
    app()