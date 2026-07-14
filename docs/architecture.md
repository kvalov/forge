# Forge Architecture

> Version: v0.3 Alpha

This document defines the architectural principles of Forge.

---

# Vision

Forge is a **Software Knowledge Engine**.

Its goal is to understand software projects through static analysis and expose that knowledge to different clients:

- CLI
- AI agents
- IDE extensions
- APIs
- CI/CD integrations

The AI layer consumes knowledge. It does not create it.

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
Infrastructure
```

Dependencies always point downward.

---

# Project Structure

```
forge/

    cli/

    project/

    workspace/

    repository/

    python/

    infrastructure/

    logging/

    errors/
```

Each package owns its own domain.

---

# Package Responsibilities

## cli

Responsible for:

- parsing CLI arguments
- formatting output
- calling application services

No business logic.

---

## project

Responsible for project-wide analysis.

Owns:

- ProjectScanner
- ProjectAnalyzer
- ProjectService

---

## workspace

Responsible for:

- workspace discovery
- ignore rules
- filesystem traversal

---

## repository

Responsible for:

- Git metadata
- repository information

---

## python

Responsible for:

- parsing
- AST analysis
- symbol indexing
- import graph
- reference graph

No dependency on CLI.

No dependency on Git.

---

## infrastructure

Contains adapters for external systems.

Examples:

- GitPython
- Local filesystem

No domain logic.

---

# Dependency Rules

Allowed

CLI
→ Project

Project
→ Workspace

Project
→ Python

Project
→ Repository

Infrastructure
→ External libraries

Forbidden

Python
→ CLI

Python
→ Repository

Workspace
→ CLI

Repository
→ Python

Infrastructure
→ Project

---

# Models

Models represent domain concepts.

Examples

- ModuleInfo
- ProjectInfo
- ProjectAnalysis
- SymbolIndex
- Reference
- Import

Avoid wrapper models unless they introduce new behaviour.

---

# Visitors

Visitors inspect AST nodes.

Visitors must not:

- access Git
- print output
- read arbitrary files
- write files

Visitors analyze syntax only.

---

# Indexers

Indexers transform many modules into searchable structures.

Examples:

- SymbolIndex
- ImportGraph
- ReferenceGraph

Indexers are pure.

---

# Analyzer

Analyzers aggregate information.

They orchestrate:

- parser
- visitors
- indexers

---

# Services

Services orchestrate domains.

Services should not duplicate domain logic.

---

# Testing

Every feature must include:

- Ruff clean
- MyPy clean
- Pytest clean

Green build is mandatory.

---

# Pull Requests

One PR = one feature.

Every PR must:

- compile
- pass Ruff
- pass MyPy
- pass Pytest

Avoid unrelated refactoring.

---

# Design Principles

- Keep components small.
- Prefer composition over inheritance.
- Avoid duplicate parsing.
- Keep domain models immutable.
- Keep infrastructure replaceable.

---

# Long-term Vision

Forge evolves in four stages:

1. Static Analysis
2. Project Intelligence
3. Knowledge Graph
4. AI Engineering Platform

Knowledge first.

AI second.