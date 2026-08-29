# Deleting Work Items

Use this document only when explicitly deleting an existing work item.

## Explicit confirmation

Deletion must be explicitly requested.

Do not infer deletion from requests such as:

* "cancel this task";
* "close this task";
* "mark this as done";
* "remove it from the current sprint".

Those operations do not necessarily mean deleting the file.

## Before deleting

1. Locate the work item.
2. Read the work item file.
3. Read `.agent/invariants.md`.
4. Read `.agent/links.md`.
5. Search the entire repository for references to the work item.
6. Identify all pages that reference it.
7. Identify all work items that reference it as a parent or relation.

## Relationships

Before deleting the work item:

* remove it from every page's `workitems` list;
* remove or update references from other work items;
* handle parent/child relationships;
* handle work item relations.

Do not leave dangling references.

## Parent/child relationships

If other work items have:

```yaml
parent: PET-123
```

they must be handled before deleting `PET-123`.

Do not silently delete or reparent child work items.

If the user did not specify how children should be handled, stop and ask for clarification.

## Relations

If other work items refer to the deleted work item through `relations`, remove those references.

Do not silently change the semantics of unrelated relations.

## Page relationships

Remove the deleted work item from every page's `workitems` list.

Do not leave the relationship on the page after the work item is deleted.

## Delete

Only after all inbound references have been handled:

1. Delete the work item file.
2. Search again for the old path and identifier.
3. Verify that no dangling references remain.

## After deletion

Validate the affected project using `.agent/validation.md`.

Do not report successful deletion while references to the deleted file remain.

## Important

Deleting a file is different from changing its state.

Never replace an explicit delete request with:

```yaml
state: Cancelled
```

unless the user explicitly asks for that behavior.
