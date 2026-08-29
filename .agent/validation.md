# Validation

Validation should be performed after creating, editing, moving, or deleting repository data.

## Required checks

Verify:

* YAML frontmatter is valid;
* required fields are present;
* work item identifiers match filenames;
* referenced work items exist;
* referenced pages exist;
* parent work items exist;
* parent pages exist;
* no duplicate work item identifiers exist;
* no duplicate page slugs exist within the same flow directory;
* cross-links are bidirectional;
* enum values are valid according to `project.md`;
* immutable IDs were preserved;
* `created_at` was preserved;
* page filenames were not changed unintentionally;
* no dangling references remain.

## Scope of validation

For a single-file change, validate the changed file and every file directly affected by its relationships.

For a multi-file change, validate all affected files.

For operations involving renames or deletions, search the entire repository for references to the old path or identifier.

## Cross-link validation

For every work item:

```yaml
pages:
  - PET/pages/example.md
```

verify that the page contains:

```yaml
workitems:
  - PET/workitems/<workitem>.md
```

For every page:

```yaml
workitems:
  - PET/workitems/example.md
```

verify that the work item contains:

```yaml
pages:
  - PET/pages/<page>.md
```

## Enum validation

Before changing:

* `state`
* `type`
* `labels`

read the relevant project's `project.md`.

Compare values exactly, including capitalization.

## Duplicate detection

Work item identifiers must be unique.

Page slugs must be unique within their flow directory (e.g. each flow may
have its own `index.md`; that is not a collision).

UUIDs must be unique within their object type and preferably across the project.

## Failure handling

If validation fails:

1. Do not claim the operation is complete.
2. Fix the issue if it was introduced by the current operation.
3. If the issue existed before the operation and is unrelated, report it.
4. Do not make broad unrelated repairs just to make validation pass.
