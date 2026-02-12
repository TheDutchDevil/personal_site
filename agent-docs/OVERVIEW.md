# Project Overview

This is Nathan Cassee's personal academic website, hosted at [cassee.dev](https://cassee.dev).

## Technology Stack

- **Static Site Generator**: Jekyll
- **Theme**: Based on [Academic Pages](https://academicpages.github.io/) (forked from Minimal Mistakes)
- **Hosting**: GitHub Pages
- **Domain**: cassee.dev (configured via CNAME file)

## Purpose

The site serves as an academic portfolio showcasing:
- Publications (journal articles, conference papers, preprints)
- Teaching experience
- Professional service (reviewing, program committees)
- Awards and recognition

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `_pages/` | Static pages (about, publications list, etc.) |
| `_publications/` | Individual publication entries (auto-generated) |
| `_teaching/` | Teaching entries |
| `_service/` | Professional service entries (auto-generated) |
| `_awards/` | Awards and recognition |
| `_layouts/` | HTML templates for different page types |
| `_includes/` | Reusable HTML components |
| `_data/` | YAML data files (navigation, authors) |
| `markdown_generator/` | Python scripts to generate markdown from JSON |
| `files/` | PDF papers and downloadable files |
| `images/` | Site images |

## Content Generation

Publications and service entries are auto-generated from JSON files:
- `markdown_generator/publications.json` -> `_publications/*.md`
- `markdown_generator/service.json` -> `_service/*.md`

A GitHub Actions workflow (`generate-files.yml`) runs these scripts automatically when the JSON files change.
