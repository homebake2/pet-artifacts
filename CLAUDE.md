# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Purpose

This repository stores requirement pages for the `pet-mono` project as plain Markdown files.

The repository is the local source of truth for the data stored in these files. Claude Code should read and modify the files directly rather than relying on an external tracker.

This file defines repository-level rules and routes operations to the relevant instructions in `.agent/`.

Detailed schema, invariants, operation-specific rules, validation, and query examples are stored in `.agent/`.

## Repository layout

<project-key>/
  project.md
  pages/
    <flow>/
      <slug>.md

Pages are grouped into subdirectories by flow (feature area), e.g. `auth/`,
`calendar/`, `pets/`, `profile/`. Cross-cutting pages go under `common/`.

The repository may contain one or more project directories.

## Instruction routing

Before performing an operation on repository data, first identify the operation:

- create
- edit
- delete

Then read the instructions required for that operation.

Do not read or apply operation-specific instructions for unrelated operations.

### Base instructions

Before creating, editing, moving, or deleting repository data, read:

- `.agent/schema.md`
- `.agent/invariants.md`

These define the data model and rules that must remain valid.

### Page operations

For creating a page, read:

- `.agent/pages/create.md`

For editing a page, read:

- `.agent/pages/edit.md`

For deleting a page, read:

- `.agent/pages/delete.md`

### Validation

After creating, editing, moving, or deleting repository data, read:

- `.agent/validation.md`

Use it to validate the affected files before considering the operation complete.

### Queries

When searching or filtering repository data, use:

- `.agent/queries.md`

Only use this file when repository search or filtering instructions are needed.

## Operation examples

The following examples illustrate the instruction routing rules.

### Edit a requirement page

For:

Update requirement "Example".

The relevant operation is:

object: page
operation: edit

Read:

.agent/schema.md
.agent/invariants.md
.agent/pages/edit.md
.agent/validation.md

Do not read:

.agent/pages/create.md
.agent/pages/delete.md

### Delete a requirement page

For:

Delete requirement "Example".

The relevant operation is:

object: page
operation: delete

Read:

.agent/schema.md
.agent/invariants.md
.agent/pages/delete.md
.agent/validation.md

## Requirement pages describe target state, not migration

A requirement page (`pages/`) must describe the state the system is required to be in — not how the system gets there from its current state.

Do not put into a requirement page:

* narrative framing like "проблема" / "решение" / "было — стало" describing a change;
* migration mechanics (SQL migration steps, rename/backfill procedures) as the primary content of a requirement — describe only the resulting schema/behavior if a schema/behavior fact must be stated.

An exception already established in this repository: a page may contain a short "Известный пробел в реализации" ("known implementation gap") section when the requirement is not yet implemented and the gap itself needs tracking — this still states what's required and what's currently missing, not a change narrative. Do not use this as a template for describing arbitrary migrations; keep it to cases where a requirement genuinely isn't implemented yet.

## References must not point outside the repository

Never write a reference (in a page or any other file here) to a resource outside this repository — a local scratch directory, a temp path, or anything else not stored in this repo. Such references go stale immediately for anyone (or any future session) reading the file without that resource. Point at another file actually in this repo instead, or inline the information.

## General editing principles

Make the smallest change necessary to satisfy the user's request.

Preserve unrelated data, content, and formatting.

Do not rewrite or reformat unrelated files.

Do not silently fix unrelated inconsistencies unless:

- the requested operation requires the fix to preserve a repository invariant; or
- the user explicitly requested the fix.

Preserve existing UUIDs, identifiers, page filenames, and creation timestamps unless the operation-specific instructions explicitly allow changing them.

## Completion

Do not consider a create, edit, move, or delete operation complete until the relevant validation rules in `.agent/validation.md` have been satisfied.

If validation reveals an issue introduced by the current operation, fix it before reporting success.

If an unrelated pre-existing issue prevents validation, do not silently modify unrelated data. Report the issue.

## Sync

Synchronization with an external tracker is outside the scope of this repository contract unless explicitly documented elsewhere.