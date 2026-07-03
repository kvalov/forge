# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by **Keep a Changelog** and the project follows **Semantic Versioning** where applicable.

---

## [Unreleased]

### Planned
- Git Service
- Filesystem Service
- Terminal Service
- Task Engine
- Project Analyzer
- Symbol Index
- AST Parser
- Planner
- Coder
- Reviewer

---

## [v0.1.0-foundation] - 2026-07-04

### Added

#### Bootstrap
- Initial Git repository
- Python project initialized with uv
- `src` layout
- Virtual environment support
- CLI entry point

#### Doctor
- Environment diagnostics
- Python version detection
- Git version detection
- uv detection
- Virtual environment detection
- Workspace detection
- Project detection

#### Configuration
- Centralized settings using `pydantic-settings`

#### Logging
- Centralized logging
- structlog integration
- Timestamped console logging

### Infrastructure
- Hatchling build system
- Ruff
- Pytest
- MyPy
- Editable installation