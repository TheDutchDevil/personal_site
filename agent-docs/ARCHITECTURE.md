# Site Architecture

## Jekyll Collections

The site uses Jekyll collections to organize different content types. Collections are defined in `_config.yml`:

```yaml
collections:
  teaching:
    output: true
    permalink: /:collection/:path/
  publications:
    output: true
    permalink: /:collection/:path/
  awards:
    output: true
    permalink: /:collection/:path
  service:
    output: true
    permalink: /:collection/:path/
```

Each collection has its own directory prefixed with underscore (e.g., `_publications/`).

## Layouts

Layouts in `_layouts/` define page templates:

| Layout | Used For |
|--------|----------|
| `default.html` | Base layout with HTML structure |
| `single.html` | Standard content pages |
| `paper-detail.html` | Individual publication pages |
| `publications-overview.html` | Publications listing page |
| `service-overview.html` | Service listing page |
| `talk.html` | Talk/presentation pages |

## Includes

Reusable components in `_includes/`:

- `author-profile.html` - Sidebar with author info and social links
- `masthead.html` - Site header with navigation
- `footer.html` - Site footer
- `slim-pub.html` - Compact publication display
- `slim-service.html` - Compact service display
- `slim-award.html` - Compact award display

## Navigation

Site navigation is configured in `_data/navigation.yml`:

```yaml
main:
  - title: "Publications"
    url: /publications/
  - title: "Teaching"
    url: /teaching/
  - title: "Service"
    url: /service/
  - title: "Recognition"
    url: /recognition/
```

## Configuration

Main site configuration lives in `_config.yml`:
- Site metadata (title, description, URL)
- Author information (bio, social links, avatar)
- Collection definitions
- Default layouts for each content type
- Plugin configuration
