# Content Management

## Adding Publications

Publications are auto-generated from `markdown_generator/publications.json`.

### JSON Structure

```json
{
  "publications": [
    {
      "id": "unique-slug",
      "title": "Paper Title",
      "authors": ["First Last", "Another Author"],
      "date": "2024-01-15",
      "type": "conference",
      "venue": "Conference Name",
      "filename": "paper.pdf"
    }
  ]
}
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | URL slug and filename identifier |
| `title` | Yes | Full paper title |
| `authors` | Yes | Array of author names |
| `date` | Yes | Publication date (YYYY-MM-DD) |
| `type` | Yes | Type: "conference", "journal", "preprint" |
| `venue` | No | Conference/journal name |
| `filename` | Yes | PDF filename in `files/` directory |
| `slides_url` | No | URL to presentation slides |
| `repo_url` | No | URL to code repository |

### Workflow

1. Add paper PDF to `files/` directory
2. Add entry to `markdown_generator/publications.json`
3. Commit and push - GitHub Actions generates the markdown automatically

## Adding Service Entries

Service entries are auto-generated from `markdown_generator/service.json`.

## Adding Teaching Entries

Create markdown files directly in `_teaching/` with front matter:

```yaml
---
title: "Course Name"
collection: teaching
type: "Course type"
permalink: /teaching/course-slug
venue: "University Name"
date: 2024-01-01
---

Course description here.
```

## Adding Awards

Create markdown files in `_awards/` with front matter:

```yaml
---
title: "Award Name"
collection: awards
date: 2024-01-01
---

Award description here.
```

## Editing Static Pages

Static pages live in `_pages/`:
- `about.md` - Home/about page
- `publications.md` - Publications listing
- `service.md` - Service listing
- `awards.md` - Awards listing

## Updating Author Info

Edit the `author:` section in `_config.yml`:

```yaml
author:
  name: "About me"
  avatar: "portrait.jpg"
  bio: "Your bio here"
  location: "City, Country"
  email: "email@example.com"
  googlescholar: "https://scholar.google.com/..."
  github: "username"
  twitter: "username"
  linkedin: "profile-id"
```
