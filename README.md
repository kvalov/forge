# Forge

> AI-first software engineering platform for understanding, analyzing and evolving codebases.

Forge is a modern software engineering toolkit built around **Clean Architecture**, **Domain-Driven Design** and **AI-assisted development**.

The long-term vision is to provide an intelligent engineering platform capable of understanding an entire software project, planning changes, reviewing code and eventually implementing features autonomously.

---

# Current Status

Current release:

**v0.2 Alpha**

Implemented:

- ✅ Bootstrap
- ✅ Configuration
- ✅ Structured Logging
- ✅ Doctor
- ✅ Repository
- ✅ Workspace
- ✅ Project Scanner
- ✅ Python Parser
- ✅ Symbol Index

Currently in development:

- 🚧 Code Intelligence

---

# Features

## Doctor

Verify the development environment.

```bash
forge doctor
```

Example:

```
Forge Doctor v0.2

Python       : 3.12.7
Git          : git version 2.38
uv           : 0.11.x
Workspace    : E:\Projects\forge

Status       : HEALTHY
```

---

## Repository

Inspect the current Git repository.

```bash
forge repository status
```

Example:

```
Repository : forge

Branch     : feature/bootstrap

Modified   : 2

Staged     : 0

Untracked  : 4
```

---

## Workspace

Inspect the current workspace.

```bash
forge workspace info
```

Example:

```
Workspace

Root

Python files

Directories

Tests
```

---

## Project

Scan the current project.

```bash
forge project info
```

Analyze the project.

```bash
forge project analyze
```

---

## Symbols

Build a Python symbol index.

```bash
forge symbols list
```

Search for a symbol.

```bash
forge symbols find WorkspaceService
```

---

# Architecture

Forge follows a layered architecture.

```
CLI
        │
        ▼
Application Services
        │
        ▼
Domain
        │
        ▼
Ports
        │
        ▼
Infrastructure
```

Current domains:

```
analysis/

doctor/

project/

python/

repository/

workspace/
```

---

# Technology

- Python 3.12+
- Typer
- GitPython
- Structlog
- Pytest
- Ruff
- MyPy

---

# Project Structure

```
src/forge/

analysis/

cli/

config/

doctor/

errors/

infrastructure/

logging/

project/

providers/

python/

repository/

services/

workspace/
```

---

# Development

Create a virtual environment.

```bash
uv sync
```

Run tests.

```bash
python -m pytest
```

Run Ruff.

```bash
python -m ruff check src tests
```

Run MyPy.

```bash
python -m mypy src
```

---

# Roadmap

## Phase 1

Completed

- Bootstrap
- Repository
- Workspace
- Project
- Python Parser
- Symbol Index

---

## Phase 2

Code Intelligence

- Import Graph
- Reference Graph
- Call Graph
- Dependency Graph

---

## Phase 3

AI Engineering

- Planner
- Reviewer
- AI Coder
- Autonomous Tasks

---

# Design Principles

Forge follows several engineering principles.

- Clean Architecture
- SOLID
- Domain Driven Design
- Ports & Adapters
- Composition over Inheritance
- Small PRs
- Test First
- Static Analysis

---

# Quality

Every pull request must pass:

```
pytest

ruff

mypy
```

before merging.

---

# License

MIT

---

# Vision

Forge is not intended to become another IDE.

The goal is to build an AI-native software engineering platform capable of understanding large codebases, reasoning about architecture and assisting developers with complex engineering tasks.

The long-term objective is an autonomous engineering agent built on top of a rich semantic model of source code.