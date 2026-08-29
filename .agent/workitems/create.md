# Creating Work Items

Use this document only when creating a new work item.

## Before creating

1. Identify the target project.
2. Read `<project-key>/project.md`.
3. Read `.agent/schema.md`.
4. Read `.agent/invariants.md`.
5. Determine the requested identifier.
6. Verify that the identifier does not already exist.
7. Verify that the target filename does not already exist.

## Project-defined values

Before writing:

* `state`
* `type`
* `labels`

verify every value against `project.md`.

Values must be copied exactly.

Do not:

* invent values;
* change capitalization;
* normalize spelling;
* assume values from another project.

## Identifier

The filename must match the identifier.

Example:

```text
identifier: PET-123
```

must be stored as:

```text
PET/workitems/PET-123.md
```

Do not use the UUID as the filename.

## UUID

Generate a new unique UUID for the work item.

Never reuse the UUID of another work item.

## Timestamps

Set:

```yaml
created_at: <current timestamp/date>
updated_at: <current timestamp/date>
```

The initial values may be identical.

## Parent

If a parent work item is specified:

1. Verify that it exists.
2. Store its human-readable identifier in `parent`.
3. Do not store its UUID or file path.

Example:

```yaml
parent: PET-100
```

## Relations

If relations are specified:

1. Verify that every target work item exists.
2. Use only supported relation types.
3. Do not invent relation types.

## Pages

If the new work item is related to requirement pages:

1. Read `.agent/links.md`.
2. Verify every page exists.
3. Add the page paths to `pages`.
4. Add the new work item path to each page's `workitems`.
5. Perform both sides in the same operation.

## Content

The body should contain the task description as ordinary Markdown.

Do not put structured metadata in the body.

Do not add unnecessary boilerplate.

## After creating

Validate the new work item according to `.agent/validation.md`.

At minimum verify:

* filename matches identifier;
* UUID is unique;
* project-defined enum values are valid;
* referenced work items exist;
* referenced pages exist;
* cross-links are bidirectional;
* required frontmatter exists.

Do not report the work item as successfully created until these checks pass.
