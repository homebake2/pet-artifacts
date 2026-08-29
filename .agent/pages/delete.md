# Deleting Requirement Pages

Use this document only when explicitly deleting an existing requirement page.

## Explicit confirmation

Deletion must be explicitly requested.

Do not infer deletion from requests such as:

* "archive this page";
* "remove this requirement";
* "deprecate this page".

Those may require a content or metadata change instead of deleting the file.

## Before deleting

1. Locate the page.
2. Read the page file.
3. Read `.agent/invariants.md`.
4. Read `.agent/links.md`.
5. Search the entire repository for references to the page.
6. Identify all work items referencing it.
7. Identify any child pages through `parent_page`.

## Work item relationships

Before deleting the page:

* remove it from every work item's `pages` list;
* verify that no work item still references the page.

Do not leave dangling references.

## Child pages

If other pages use:

```yaml
parent_page: PET/pages/example.md
```

for the page being deleted, they must be handled before deletion.

Do not silently reparent child pages.

If the user did not specify what should happen to child pages, stop and ask for clarification.

## Delete

Only after all inbound references have been handled:

1. Delete the page file.
2. Search again for the old path.
3. Verify that no references remain.

## After deletion

Validate the affected project according to `.agent/validation.md`.

Do not report successful deletion while references to the deleted page remain.

## Important

Deleting a page is different from removing or rewriting its content.

Never silently replace an explicit deletion request with an empty page or a deprecation marker.
