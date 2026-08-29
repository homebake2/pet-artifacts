# Editing Requirement Pages

Use this document only when editing an existing requirement page.

## Before editing

1. Locate the page file.
2. Read the existing page.
3. Read `.agent/schema.md`.
4. Read `.agent/invariants.md`.
5. If changing relationships, read `.agent/links.md`.

## Immutable fields

Do not change:

* `id`
* `created_at`
* page filename/slug

during an ordinary edit.

## Title changes

The `title` field may change.

Changing the title must NOT rename the page file.

Example:

```text
api-contract.md
```

must remain:

```text
api-contract.md
```

even if:

```yaml
title: API Contract
```

changes to:

```yaml
title: External API Contract
```

This preserves all existing references.

## Parent page

If changing `parent_page`:

1. Verify the new parent exists.
2. Verify that the change does not create a circular hierarchy.
3. Use a repository-root-relative path.

## Work item relationships

If changing `workitems`:

1. Read `.agent/links.md`.
2. Verify all referenced work items exist.
3. Update corresponding work item `pages` fields.
4. Perform both sides in the same operation.

Never leave a one-sided relationship.

## Content

Preserve unrelated requirement content.

When editing content:

* keep it as ordinary Markdown;
* preserve existing structure where possible;
* do not rewrite unrelated sections;
* do not remove requirements unless explicitly requested.

## Timestamp

Update:

```yaml
updated_at
```

for every meaningful change.

Never change:

```yaml
created_at
```

## Minimal edit

Do not:

* rename the page because its title changed;
* regenerate its UUID;
* reorder unrelated content;
* normalize unrelated formatting;
* modify unrelated pages.

## After editing

Validate all affected files according to `.agent/validation.md`.

Do not report success if the resulting page has broken relationships or invalid references.
