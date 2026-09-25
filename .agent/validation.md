# Validation

Validation should be performed after creating, editing, moving, or deleting repository data.

## Required checks

Verify:

* YAML frontmatter is valid;
* required fields are present;
* referenced pages exist;
* parent pages exist;
* no duplicate page slugs exist within the same flow directory;
* immutable IDs were preserved;
* `created_at` was preserved;
* page filenames were not changed unintentionally;
* no dangling references remain.

## Scope of validation

For a single-file change, validate the changed file and every file directly affected by its relationships.

For a multi-file change, validate all affected files.

For operations involving renames or deletions, search the entire repository for references to the old path or identifier.

## Duplicate detection

Page slugs must be unique within their flow directory (e.g. each flow may
have its own `index.md`; that is not a collision).

UUIDs must be unique within their object type and preferably across the project.

## Failure handling

If validation fails:

1. Do not claim the operation is complete.
2. Fix the issue if it was introduced by the current operation.
3. If the issue existed before the operation and is unrelated, report it.
4. Do not make broad unrelated repairs just to make validation pass.
