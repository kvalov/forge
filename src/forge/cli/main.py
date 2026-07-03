import typer

from forge.services.doctor import check

app = typer.Typer(help="Forge AI Software Engineer")


@app.callback()
def callback() -> None:
    """Forge CLI."""
    pass


@app.command()
def doctor() -> None:
    """Run environment diagnostics."""
    raise typer.Exit(check())


def main() -> None:
    app()