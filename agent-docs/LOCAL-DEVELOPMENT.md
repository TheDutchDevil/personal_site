# Local Development

## Prerequisites

- Docker (recommended)
- OR Ruby + Bundler

## Running with Docker (Recommended)

### Build the image

```bash
docker build -t personal-site .
```

### Run the server

```bash
docker run -it --rm -p 4000:4000 personal-site
```

The site will be available at `http://localhost:4000`.

## Running with Ruby

### Install dependencies

```bash
bundle install
```

### Start the server

```bash
bundle exec jekyll serve
```

For development with live reload:

```bash
bundle exec jekyll serve --livereload
```

## Development Configuration

The file `_config.dev.yml` contains development-specific overrides. Use it with:

```bash
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

## Regenerating Content

To regenerate publications and service markdown files locally:

```bash
cd markdown_generator
pip install pandas
python publications.py
python service.py
```

## File Watching

Jekyll watches for file changes and rebuilds automatically. Note that changes to `_config.yml` require a server restart.

## Common Issues

### Changes not appearing
- Clear Jekyll's cache: `rm -rf _site .jekyll-cache`
- Restart the server

### Ruby version issues
- Check `.ruby-version` if present
- Use a Ruby version manager (rbenv, rvm)

### Bundle errors
- Run `bundle update` to update dependencies
- Delete `Gemfile.lock` and run `bundle install`
