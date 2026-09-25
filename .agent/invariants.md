# Repository Invariants

These rules must hold after every repository operation.

## Identity

1. Every page has a unique `id`.
2. Existing page UUIDs are immutable.
3. Existing page slugs/filenames are immutable.
4. `created_at` is immutable.

## References

1. Every `parent_page` reference must point to an existing page.
2. Never intentionally create dangling references.

## Page hierarchy

Pages may form a parent/child hierarchy.

A page must never be its own ancestor.

Do not create direct or indirect circular `parent_page` relationships.

## Timestamps

`created_at` never changes after creation.

`updated_at` changes whenever the file is meaningfully modified.

Reading a file does not change `updated_at`.

## File naming

Page:

```text
<flow>/<immutable-slug>.md
```

A page title change must not rename the page file.

A page's flow (its containing subdirectory under `pages/`) is treated the
same as its slug: moving a page to a different flow folder is a rename and
must not happen silently. If a page's flow changes, update every
`parent_page` reference to its new path in the same operation.

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
