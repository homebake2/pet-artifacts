# Repository Invariants

These rules must hold after every repository operation.

## Identity

1. Every work item has a unique `id`.
2. Every page has a unique `id`.
3. A work item's `identifier` matches its filename.
4. Existing work item UUIDs are immutable.
5. Existing page UUIDs are immutable.
6. Existing page slugs/filenames are immutable.
7. `created_at` is immutable.

## Project enums

1. Work item `state` must exist in `project.md.states`.
2. Every work item label must exist in `project.md.labels`.
3. Work item `type` must exist in `project.md.workitem_types`.
4. Enum values are case-sensitive.
5. Never invent or normalize enum values.

## References

1. Every `parent` reference must point to an existing work item.
2. Every work item relation must point to an existing work item.
3. Every work item `pages` reference must point to an existing page.
4. Every page `workitems` reference must point to an existing work item.
5. Every `parent_page` reference must point to an existing page.
6. Never intentionally create dangling references.

## Bidirectional relationships

For every work item/page relationship:

```text
workitem.pages
    <-> 
page.workitems
```

Both sides must contain the corresponding reference.

A relationship represented on only one side is invalid.

## Page hierarchy

Pages may form a parent/child hierarchy.

A page must never be its own ancestor.

Do not create direct or indirect circular `parent_page` relationships.

## Timestamps

`created_at` never changes after creation.

`updated_at` changes whenever the file is meaningfully modified.

Reading a file does not change `updated_at`.

## File naming

Work item:

```text
<identifier>.md
```

Page:

```text
<flow>/<immutable-slug>.md
```

A page title change must not rename the page file.

A page's flow (its containing subdirectory under `pages/`) is treated the
same as its slug: moving a page to a different flow folder is a rename and
must not happen silently. If a page's flow changes, update every
`parent_page` and `pages`/`workitems` reference to its new path in the same
operation.

## Content

Markdown bodies must remain human-readable Markdown.

Do not replace Markdown content with raw HTML, JSON, or source-system rich-text payloads.

## Scope

Do not create a separate index, manifest, cache, or generated metadata file unless explicitly requested.

Do not silently introduce new schema fields.

If a new field is required, follow the repository's existing schema conventions and make the change explicit.

## Minimal changes

Do not modify unrelated files.

Do not normalize unrelated formatting.

Do not silently repair unrelated data while performing another operation.

If an unrelated invariant violation prevents the requested operation from being completed safely, report it rather than silently changing unrelated data.
