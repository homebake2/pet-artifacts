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
  pages/
    <flow>/
```

`<project-key>` is the project identifier, for example `PET`.

Pages are grouped into subdirectories by flow (feature area), for example
`auth/`, `calendar/`, `pets/`, `profile/`. Cross-cutting pages that don't
belong to a single flow live under `common/`.

## `project.md`

`project.md` contains project-level metadata.

Example:

```yaml
---
id: <uuid>
name: pet-mono
---
```

`project.md` must not contain individual page metadata.

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
