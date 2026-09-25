# Creating Requirement Pages

Use this document only when creating a new requirement page.

## Before creating

1. Identify the target project.
2. Read `.agent/schema.md`.
3. Read `.agent/invariants.md`.
4. Determine the initial page title.
5. Generate the page slug according to the repository's existing slug convention.
6. Verify that the target filename does not already exist.

## Slug

The filename is derived from the page's initial title.

Example:

```text
title: API Contract
```

may result in:

```text
api-contract.md
```

The exact slug convention should follow existing repository practice.

Once the page is created, the filename is immutable.

## UUID

Generate a new unique UUID.

Never reuse the UUID of another page.

## Timestamps

Set:

```yaml
created_at: <current timestamp/date>
updated_at: <current timestamp/date>
```

## Parent page

If `parent_page` is specified:

1. Verify the parent page exists.
2. Use a repository-root-relative path.
3. Ensure the new page does not create a circular hierarchy.

Example:

```yaml
parent_page: PET/pages/other-page.md
```

## Content

The page body must be ordinary Markdown.

Preserve the semantic structure of the requirement.

Do not store raw HTML, JSON, or source-system rich-text blocks.

## After creating

Validate according to `.agent/validation.md`.

At minimum verify:

* UUID is unique;
* filename is unique;
* parent page exists;
* no hierarchy cycle exists;
* required frontmatter exists.
