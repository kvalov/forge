from __future__ import annotations

import typer

from forge.infrastructure.filesystem.local_filesystem_adapter import (
    LocalFilesystemAdapter,
)
from forge.project.analyzer import ProjectAnalyzer
from forge.project.scanner import ProjectScanner
from forge.project.service import ProjectService
from forge.workspace.service import WorkspaceService

app = typer.Typer(help="Project commands")


def _service() -> ProjectService:
    workspace = WorkspaceService(
        LocalFilesystemAdapter()
    )

    scanner = ProjectScanner(workspace)
    analyzer = ProjectAnalyzer(workspace)

    return ProjectService(
        scanner=scanner,
        analyzer=analyzer,
    )


@app.command("info")
def info() -> None:
    project = _service().info()

    typer.echo()
    typer.echo("Project")
    typer.echo("─" * 40)

    typer.echo(f"Name          : {project.name}")
    typer.echo(f"Root          : {project.root}")

    typer.echo()
    typer.echo(f"Files         : {project.total_files}")
    typer.echo(f"Python Files  : {project.python_files}")
    typer.echo(f"Test Files    : {project.test_files}")

    typer.echo()
    typer.echo(f"Git           : {'YES' if project.has_git else 'NO'}")
    typer.echo(f"pyproject     : {'YES' if project.has_pyproject else 'NO'}")
    typer.echo(f"README        : {'YES' if project.has_readme else 'NO'}")


@app.command("analyze")
def analyze() -> None:
    analysis = _service().analyze()

    typer.echo()
    typer.echo("Project Analysis")
    typer.echo("─" * 40)

    typer.echo(f"Project       : {analysis.project.name}")

    typer.echo()
    typer.echo(f"Modules       : {analysis.modules}")
    typer.echo(f"Classes       : {analysis.classes}")
    typer.echo(f"Functions     : {analysis.functions}")
    typer.echo(f"Imports       : {analysis.imports}")

    typer.echo()
    typer.echo(f"Python Files  : {analysis.project.python_files}")
    typer.echo(f"Test Files    : {analysis.project.test_files}")