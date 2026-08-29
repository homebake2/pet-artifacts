# Work Item / Page Links

This document defines relationships between work items and requirement pages.

## Relationship model

Work items reference pages through:

```yaml
pages:
  - PET/pages/api-contract.md
```

Pages reference work items through:

```yaml
workitems:
  - PET/workitems/PET-123.md
```

These references are bidirectional.

## Adding a relationship

When adding:

```text
PET/workitems/PET-123.md
    ->
PET/pages/api-contract.md
```

perform both changes:

### Work item

```yaml
pages:
  - PET/pages/api-contract.md
```

### Page

```yaml
workitems:
  - PET/workitems/PET-123.md
```

Both files must be changed in the same operation.

## Removing a relationship

When removing a relationship, remove both sides in the same operation.

Do not leave:

```text
workitem -> page
```

without:

```text
page -> workitem
```

or vice versa.

## Validation

Before adding a relationship:

1. Verify the target file exists.
2. Verify the reference path is repository-root-relative.
3. Verify the relationship does not already exist.
4. Update both sides.

After changing a relationship:

1. Verify both files contain the relationship.
2. Verify both referenced files exist.
3. Verify no duplicate entries were introduced.

## File movement

If a referenced file is moved:

1. Find every reference to the old path.
2. Update all references.
3. Preserve the object's UUID.
4. Preserve the page slug if the object is a page.
5. Validate all affected relationships.

Do not leave references to the old path.

## Deletion

Before deleting a referenced file, remove all relationships pointing to it.

Deletion must not leave dangling references.
