# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Purpose

This repository stores work items and requirement pages for the `pet-mono` project as plain Markdown files.

The repository is the local source of truth for the data stored in these files. Claude Code should read and modify the files directly rather than relying on an external tracker.

This file defines repository-level rules and routes operations to the relevant instructions in `.agent/`.

Detailed schema, invariants, operation-specific rules, relationship rules, validation, and query examples are stored in `.agent/`.

## Repository layout

<project-key>/
  project.md
  workitems/
    <identifier>.md
  pages/
    <flow>/
      <slug>.md

Pages are grouped into subdirectories by flow (feature area), e.g. `auth/`,
`calendar/`, `pets/`, `profile/`. Cross-cutting pages go under `common/`.
Work items stay flat under `workitems/` — no subdirectories.

The repository may contain one or more project directories.

## Instruction routing

Before performing an operation on repository data, first identify:

1. the object type:
   - work item
   - page
2. the operation:
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

### Work item operations

For creating a work item, read:

- `.agent/workitems/create.md`

For editing a work item, read:

- `.agent/workitems/edit.md`

For deleting a work item, read:

- `.agent/workitems/delete.md`

### Page operations

For creating a page, read:

- `.agent/pages/create.md`

For editing a page, read:

- `.agent/pages/edit.md`

For deleting a page, read:

- `.agent/pages/delete.md`

### Relationships

If the operation adds, removes, or changes a relationship between a work item and a page, also read:

- `.agent/links.md`

Do not read `.agent/links.md` when the operation does not affect work item/page relationships.

### Validation

After creating, editing, moving, or deleting repository data, read:

- `.agent/validation.md`

Use it to validate the affected files and relationships before considering the operation complete.

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

If the edit changes work item/page relationships, also read:

.agent/links.md

Do not read:

.agent/pages/create.md
.agent/pages/delete.md
.agent/workitems/create.md
.agent/workitems/edit.md
.agent/workitems/delete.md

### Create a work item

For:

Create task PET-123.

The relevant operation is:

object: work item
operation: create

Read:

.agent/schema.md
.agent/invariants.md
.agent/workitems/create.md
.agent/validation.md

If the task is linked to a requirement page, also read:

.agent/links.md

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
.agent/links.md
.agent/validation.md

## Project metadata

Each project has a `project.md`.

`project.md` is the authoritative source for:

- valid work item states;
- valid labels;
- valid work item types.

These values are case-sensitive.

Never invent, normalize, or silently change these values.

Before creating or changing a work item's `state`, `labels`, or `type`, read the relevant `<project-key>/project.md` and use only values defined there.

Do not assume that enum values are the same across projects.

## Requirement pages describe target state, not migration

A requirement page (`pages/`) must describe the state the system is required to be in — not how the system gets there from its current state.

Do not put into a requirement page:

* narrative framing like "проблема" / "решение" / "было — стало" describing a change;
* references to a change being made "в рамках PET-123" or similar transition language;
* migration mechanics (SQL migration steps, rename/backfill procedures) as the primary content of a requirement — describe only the resulting schema/behavior if a schema/behavior fact must be stated.

That information belongs in the work item (task) that implements the change. A work item description is the right place for "how to get from current state to required state" — migration steps, affected files, rollout order, dependencies between tasks.

An exception already established in this repository: a page may contain a short "Известный пробел в реализации" ("known implementation gap") section when the requirement is not yet implemented and the gap itself needs tracking — this still states what's required and what's currently missing, not a change narrative. Do not use this as a template for describing arbitrary migrations; keep it to cases where a requirement genuinely isn't implemented yet.

A page may reference a work item by identifier (e.g. "см. PET-123") the same way existing pages do, as a pointer for where implementation work is tracked — that is fine. What's not fine is explaining the mechanics of that work inside the requirement text itself.

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