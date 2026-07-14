# Contributing to Forge

Thank you for contributing to Forge.

---

# Development Workflow

Every change should follow this order:

1. Write code
2. Run Ruff
3. Run MyPy
4. Run Pytest
5. Commit

---

# Code Style

- Python 3.12+
- Type hints required
- Frozen dataclasses preferred
- Small focused classes
- Explicit dependencies

---

# Naming

Classes

```
ProjectAnalyzer
WorkspaceService
ReferenceGraph
```

Methods

```
analyze()
build()
parse()
```

Tests

```
test_project_analyzer.py
test_reference_graph.py
```

---

# Pull Requests

One feature per PR.

Avoid mixing:

- refactoring
- bug fixes
- new features

---

# Quality Gates

Every PR must pass:

```
python -m ruff check src tests

python -m mypy src

python -m pytest
```

---

# Architecture

Read:

docs/ARCHITECTURE.md

before implementing new functionality.

---

# Philosophy

Forge is built around understanding software.

Every feature should improve project understanding before automation.

Knowledge first.

Automation second.