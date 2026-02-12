# Deployment

## GitHub Pages

The site is automatically deployed via GitHub Pages when changes are pushed to the `master` branch.

### How it works

1. Push commits to `master` branch
2. GitHub Pages builds the Jekyll site
3. Site is deployed to `https://cassee.dev`

### Custom Domain

The custom domain is configured via:
- `CNAME` file containing `cassee.dev`
- DNS records pointing to GitHub Pages servers

## Automated Content Generation

A GitHub Actions workflow automatically generates publication and service markdown files.

### Workflow: `.github/workflows/generate-files.yml`

**Trigger**: Push to `markdown_generator/**`

**Steps**:
1. Checkout repository
2. Setup Python
3. Install pandas
4. Run `publications.py` and `service.py`
5. Commit and push generated files

### Workflow triggers

The workflow runs when files in `markdown_generator/` change:
- `publications.json`
- `service.json`
- Python scripts

## Manual Deployment Steps

For most content updates:

1. Make changes (edit JSON, add files, modify pages)
2. Commit changes
3. Push to `master`
4. GitHub Pages automatically rebuilds

For publication updates specifically:

1. Add PDF to `files/`
2. Update `markdown_generator/publications.json`
3. Commit and push
4. GitHub Actions generates markdown
5. GitHub Pages deploys

## Repository Settings

Key GitHub repository settings:
- **Repository**: `thedutchdevil/personal_site`
- **Default branch**: `master`
- **GitHub Pages source**: `master` branch

## Verifying Deployment

After pushing:
1. Check GitHub Actions for workflow status
2. Wait 1-2 minutes for GitHub Pages build
3. Visit `https://cassee.dev` to verify changes
4. Hard refresh (Ctrl+Shift+R) to bypass cache
