# Forge Architecture

> "Software engineering for AI begins with understanding the code."

---

# Overview

Forge is built around a simple idea:

**AI cannot safely modify software it does not understand.**

Before planning, reviewing or generating code, Forge must build an internal semantic model of the project.

Everything inside Forge exists to support that objective.

---

# Core Principles

Forge follows several architectural principles.

- Clean Architecture
- Domain-Driven Design
- SOLID
- Ports & Adapters
- Composition over Inheritance
- Explicit Dependencies
- Testability First
- Static Analysis

---

# High-Level Architecture

```
                CLI
                 │
                 ▼
         Application Services
                 │
                 ▼
        Domain / Business Logic
                 │
                 ▼
         Ports (Interfaces)
                 │
                 ▼
      Infrastructure Adapters
```

The domain never depends on infrastructure.

Infrastructure depends on the domain.

The CLI depends only on services.

---

# Current Domains

```
analysis/
doctor/
project/
python/
repository/
workspace/
```

Each domain has a single responsibility.

---

# Repository Domain

Responsible for understanding Git repositories.

```
RepositoryService
        │
        ▼
RepositoryPort
        │
        ▼
GitPythonAdapter
```

Responsibilities

- Repository status
- Branch information
- Working tree
- Remote detection

Future

- Commit history
- Branch comparison
- Diff analysis

---

# Workspace Domain

Responsible for understanding the filesystem.

```
WorkspaceService
        │
        ▼
WorkspacePort
        │
        ▼
LocalFilesystemAdapter
```

Responsibilities

- Project root
- Python files
- Ignore rules
- File discovery

Future

- File watching
- Cache
- Workspace snapshots

---

# Project Domain

Responsible for project-level information.

```
ProjectService
        │
        ▼
ProjectScanner
        │
        ▼
WorkspaceService
```

Responsibilities

- Project metadata
- Statistics
- Project analysis

Future

- Complexity
- Metrics
- Project health

---

# Python Domain

Responsible for understanding Python source code.

```
Python Source

        │

        ▼

Parser

        │

        ▼

AST

        │

 ┌──────┴─────────┐

 ▼                ▼

ModuleVisitor   SymbolVisitor

 │                │

 ▼                ▼

ModuleInfo    SymbolIndex
```

Responsibilities

- Parsing
- Symbol indexing
- AST analysis

Future

- Import graph
- Reference graph
- Call graph

---

# Doctor Domain

Responsible for validating the environment.

```
DoctorService

        │

        ▼

DoctorRunner

        │

 ┌──────┴────────────┐

 ▼                   ▼

DoctorCheck      DoctorReport
```

Checks

- Python
- Git
- uv
- Workspace

Future

- Cache
- Plugins
- Configuration
- AI providers

---

# Analysis Domain

Current purpose

Aggregate project information.

Future purpose

Become the language-independent analysis engine.

```
analysis/

    python/

    imports/

    references/

    callgraph/
```

---

# Infrastructure

Infrastructure contains implementations.

```
GitPythonAdapter

LocalFilesystemAdapter
```

Infrastructure never contains business logic.

---

# Dependency Rule

Allowed

```
CLI

↓

Services

↓

Domain

↓

Ports

↓

Infrastructure
```

Forbidden

```
Infrastructure

↓

CLI
```

---

# Python Analysis Pipeline

Current

```
Workspace

↓

PythonIndexer

↓

IndexBuilder

↓

SymbolVisitor

↓

SymbolIndex
```

Future

```
Workspace

↓

Python Parser

↓

AST

↓

ImportVisitor

↓

ReferenceVisitor

↓

CallVisitor

↓

ArchitectureBuilder

↓

Knowledge Graph
```

---

# Future AI Pipeline

```
Knowledge Graph

↓

Planner

↓

Reviewer

↓

AI Coder

↓

Task Engine
```

Every AI capability will rely on the semantic model produced by the analysis pipeline.

---

# Long-Term Vision

Forge is not a code generator.

Forge is a software engineering platform.

The objective is to understand a software system before proposing or applying changes.

Understanding precedes generation.

Analysis precedes automation.

This principle guides every architectural decision inside Forge.