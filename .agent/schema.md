# Repository Schema

This document defines the file formats used by the repository.

## General format

All data files are Markdown files with YAML frontmatter.

Structured metadata belongs in YAML frontmatter.

Human-readable content belongs in the Markdown body.

The Markdown body must contain ordinary Markdown, not raw source-system payloads.

## Project structure

Each project has:

```text
<project-key>/
  project.md
  workitems/
  pages/
    <flow>/
```

`<project-key>` is the project identifier, for example `PET`.

Pages are grouped into subdirectories by flow (feature area), for example
`auth/`, `calendar/`, `pets/`, `profile/`. Cross-cutting pages that don't
belong to a single flow live under `common/`. Work items are not grouped
into subdirectories — they stay flat under `workitems/`.

## `project.md`

`project.md` contains project-level metadata.

Example:

```yaml
---
id: <uuid>
name: pet-mono
states:
  - Backlog
  - In Progress
  - Done
labels:
  - backend
  - frontend
  - infrastructure
workitem_types:
  - Task
  - Bug
  - Epic
---
```

The exact values are project-specific.

### Authoritative fields

The following fields define valid values used by work items:

* `states`
* `labels`
* `workitem_types`

These values are case-sensitive.

`project.md` must not contain individual work item or page metadata.

---

## Work item files

Path:

```text
<project-key>/workitems/<identifier>.md
```

Example:

```text
PET/workitems/PET-123.md
```

Example content:

```yaml
---
id: <uuid>
identifier: PET-123
type: Task
title: Example task
state: In Progress
priority: High
assignee: oleg.kaliugin.oka@gmail.com
labels:
  - backend
parent: PET-100
relations:
  blocks:
    - PET-130
pages:
  - PET/pages/auth/api-contract.md
created_at: 2026-08-10
updated_at: 2026-08-27
---

Description of the task as free-form Markdown.

## Comments

- 2026-08-15 oleg: Example comment.
```

### Work item fields

#### `id`

UUID of the work item.

Required.

#### `identifier`

Human-readable work item identifier such as `PET-123`.

Required.

The identifier must match the filename.

#### `type`

Work item type.

Required.

Must match one of `project.md.workitem_types`.

#### `title`

Work item title.

Required.

#### `state`

Current work item state.

Required.

Must match one of `project.md.states`.

#### `priority`

Work item priority.

Required unless the existing project schema explicitly treats it as optional.

Use the representation already established by the repository/project.

#### `assignee`

Current assignee.

Its representation must remain consistent with the repository.

#### `labels`

List of labels.

Labels must be defined by `project.md.labels`.

An empty list should normally be represented as:

```yaml
labels: []
```

#### `parent`

Optional parent work item identifier.

Example:

```yaml
parent: PET-100
```

The referenced work item must exist.

#### `relations`

Optional relationships to other work items.

Example:

```yaml
relations:
  blocks:
    - PET-130
```

Each referenced work item must exist.

Only supported relation types may be used.

#### `pages`

Optional list of related requirement pages.

Paths are relative to the repository root.

Example:

```yaml
pages:
  - PET/pages/auth/api-contract.md
```

Each referenced page must exist.

The corresponding page must contain the reverse relationship in its `workitems` field.

#### `created_at`

Creation date/timestamp.

Required.

#### `updated_at`

Last meaningful modification date/timestamp.

Required.

---

## Page files

Path:

```text
<project-key>/pages/<flow>/<slug>.md
```

`<flow>` is the feature area the page belongs to (`auth`, `calendar`, `pets`,
`profile`, ...). Pages that don't belong to a single flow go under
`common/`.

Example:

```text
PET/pages/auth/api-contract.md
```

Example:

```yaml
---
id: <uuid>
title: API Contract
parent_page: PET/pages/auth/other-page.md
workitems:
  - PET/workitems/PET-123.md
created_at: 2026-08-10
updated_at: 2026-08-27
---

# API Contract

Page content as free-form Markdown.
```

### Page fields

#### `id`

UUID of the page.

Required.

#### `title`

Current page title.

Required.

#### `parent_page`

Optional repository-root-relative path to the parent page.

The referenced page must exist.

#### `workitems`

List of related work item paths.

Each referenced work item must exist.

Each relationship must also exist in the work item's `pages` field.

#### `created_at`

Creation date/timestamp.

Required.

#### `updated_at`

Last meaningful modification date/timestamp.

Required.

---

## Markdown content

Descriptions and page content must be ordinary Markdown.

When converting rich text from an external system:

* convert headings to Markdown headings;
* convert lists to Markdown lists;
* preserve links as Markdown links;
* preserve code as fenced code blocks;
* preserve tables where practical;
* preserve meaningful emphasis;
* preserve the semantic structure of the original content.

Do not store raw HTML, rich-text block JSON, or proprietary serialized content in the Markdown body unless explicitly required.

## YAML conventions

Use valid YAML frontmatter.

Unless an existing repository convention says otherwise:

* use ISO 8601-compatible dates/timestamps;
* use `[]` for empty lists;
* use `null` for explicitly unknown scalar values;
* preserve existing field order;
* preserve existing formatting style where practical.

Do not change the representation of existing fields without a reason.

For example, do not switch between:

```yaml
labels: []
```

and:

```yaml
labels:
```

without an explicit reason.
