# Common Queries

Run commands from the repository root.

These examples assume project key `PET`.

## Work items by state

```bash
grep -l '^state: In Progress$' PET/workitems/*.md
```

## Work items by assignee

```bash
grep -l '^assignee: oleg.kaliugin.oka@gmail.com$' PET/workitems/*.md
```

## Children of a work item

```bash
grep -l '^parent: PET-100$' PET/workitems/*.md
```

## Pages referencing a work item

```bash
grep -l 'PET/workitems/PET-123.md' PET/pages/*/*.md
```

## Work items referencing a page

```bash
grep -l 'PET/pages/auth/api-contract.md' PET/workitems/*.md
```

## Search for a label

For a simple single-line labels field:

```bash
grep -l '^labels:.*backend' PET/workitems/*.md
```

For multi-line YAML lists, prefer a YAML-aware tool such as `yq` when available.

## Search by title

```bash
grep -l '^title:.*API' PET/workitems/*.md
```

## Search all references to a work item

```bash
grep -R 'PET/workitems/PET-123.md' PET/
```

## Search all references to a page

```bash
grep -R 'PET/pages/auth/api-contract.md' PET/
```

## Find work item files

```bash
find PET/workitems -name '*.md'
```

## Find page files

```bash
find PET/pages -name '*.md'
```

## Important

Broad text searches can match Markdown body content and comments.

When exact frontmatter filtering is required, use a YAML-aware tool such as `yq` when available.
