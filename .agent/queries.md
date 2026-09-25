# Common Queries

Run commands from the repository root.

These examples assume project key `PET`.

## Search by title

```bash
grep -l '^title:.*API' PET/pages/*/*.md
```

## Search all references to a page

```bash
grep -R 'PET/pages/auth/api-contract.md' PET/
```

## Find page files

```bash
find PET/pages -name '*.md'
```

## Important

Broad text searches can match Markdown body content and comments.

When exact frontmatter filtering is required, use a YAML-aware tool such as `yq` when available.
