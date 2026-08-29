# Editing Work Items

Use this document only when editing an existing work item.

## Before editing

1. Locate the work item file.
2. Read the existing file.
3. Read `.agent/schema.md`.
4. Read `.agent/invariants.md`.
5. If changing page relationships, read `.agent/links.md`.
6. If changing `state`, `type`, or `labels`, read the project's `project.md`.

## Immutable fields

Do not change the following fields during an ordinary edit:

* `id`
* `created_at`

Do not change the work item's identifier or filename unless the user explicitly requests an identifier change.

## Identifier changes

Changing an identifier is a special operation.

If explicitly requested:

1. Preserve the existing UUID.
2. Change `identifier`.
3. Rename the file to match the new identifier.
4. Find all references to the old work item path.
5. Update all affected references.
6. Preserve page relationships.
7. Update `updated_at`.
8. Validate the repository.

Do not change an identifier merely because the title changed.

## Title changes

Changing `title` does not change the filename.

Do not rename the file because the title changed.

## State, type, and labels

Before changing any of:

* `state`
* `type`
* `labels`

read `project.md`.

Use only values defined there.

Values are case-sensitive.

## Parent

If changing `parent`:

1. Verify the new parent exists.
2. Ensure the work item does not become its own ancestor if the repository uses hierarchical parent relationships.
3. Do not use a UUID or path in `parent`.

## Relations

If changing `relations`:

1. Verify all referenced work items exist.
2. Preserve supported relation semantics.
3. Do not invent relation types.

## Page relationships

If adding or removing entries in `pages`:

1. Read `.agent/links.md`.
2. Verify target pages exist.
3. Update the corresponding page `workitems` list.
4. Perform both sides in the same operation.

Never leave a one-sided relationship.

## Content

Preserve unrelated Markdown content and comments.

When modifying a description:

* preserve existing meaning unless the request asks for a rewrite;
* use ordinary Markdown;
* do not replace the entire body unnecessarily.

## Timestamp

Update:

```yaml
updated_at
```

for every meaningful edit.

Never change:

```yaml
created_at
```

## Minimal edit

Only change what is necessary for the requested operation.

Do not:

* normalize unrelated fields;
* reorder unrelated content;
* change formatting without a reason;
* repair unrelated work items;
* create new metadata fields without an explicit schema reason.

## After editing

Validate the affected files using `.agent/validation.md`.

If the edit affects cross-links or references, validate all affected files.

Do not report success if the resulting repository violates an invariant.
