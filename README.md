# seanblanchfield.com

The source for Sean Blanchfield's personal blog. A small Python generator builds the site and GitHub Actions deploys it to GitHub Pages.

- Production: [seanblanchfield.com](https://seanblanchfield.com)
- Staging: [staging.seanblanchfield.com](https://staging.seanblanchfield.com)
- Local preview: [preview.home.seanblanchfield.com](https://preview.home.seanblanchfield.com)

## Structure

```text
content/
├── posts/       # Dated Markdown articles
├── pages/       # Bio, How I work, redirects, configuration and CNAME
├── clippings/   # Press, podcasts and interviews
├── images/      # Source images
└── assets/      # Fonts, icons and favicon
code/            # Generator, preview server, styles, tests and checks
site/            # Generated output; ignored
.build-cache/    # Local rendering and thumbnail cache; ignored
```

The old Jekyll implementation remains recoverable from Git history. It is no longer a maintained working tree.

## Install

Python 3.11 or later is required.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r code/requirements.txt
```

If the system Python cannot create virtual environments, install the operating system's `python3-venv` package first.

## Add or edit content

Add an article at `content/posts/YYYY-MM-DD-title.md`:

```markdown
---
title: An example
date: 2026-10-19 12:00:00 +0100
image: /images/2026/10/example.jpg
---

Write the article here.
```

The optional front-matter fields include:

- `slug` or `permalink` to override the generated URL
- `author` to override the default author, Sean Blanchfield
- `modified_date` for a substantive revision
- `hidden: true` to keep a post reachable but remove it from listings and the feed
- `redirect_to` or `redirect_from` for moved URLs
- `image` for the article hero and listing card

Save article images under `content/images/`. The generator creates an adjacent Markdown representation for every article and publishes HTML at clean URLs such as `/2026/10/title`.

Clippings live in `content/clippings/`. Each needs `link`, `image`, `date`, `source` and `type` front matter. They render as full cards on `/clippings/`; they do not get individual pages.

## Build and preview

Run a clean build before release:

```sh
.venv/bin/python code/build.py --fail-on-drafts
```

Use the incremental build while editing:

```sh
.venv/bin/python code/build.py --fail-on-drafts --incremental
```

Incremental builds reuse rendered Markdown and content-addressed thumbnails from `.build-cache/`, update files atomically and remove stale generator-owned output. An ordinary one-page edit takes less than one second on the current workspace. A clean build recreates `site/` while still reusing cached thumbnails.

Start the local preview only if port 8765 is not already in use:

```sh
.venv/bin/python code/preview.py --bind 0.0.0.0 --port 8765
```

The preview server has no authentication. Do not put sensitive drafts in a served build. Building with `--fail-on-drafts` refuses any `draft: true` content.

## Generated site

The generator emits:

- Server-rendered semantic HTML
- Direct Markdown article alternatives
- Chronological listing pages
- Atom feed at `/feed.xml`
- XML sitemap at `/sitemap.xml`
- Crawler policy at `/robots.txt`
- LLM-oriented index at `/llms.txt`
- Schema.org JSON-LD and Open Graph metadata
- Light and dark themes
- Build-time syntax highlighting
- WebP listing-card thumbnails under `/images/_cards/`

The 94 renderable posts produce 84 chronological listing entries. Seven deliberately delisted posts remain reachable at their original URLs. `posts/2022_ezviz_db1_related_posts.md` lacks front matter and remains an intentionally ignored source fragment.

## Checks

Run these after building:

```sh
.venv/bin/python -m unittest discover -s code -p 'test_*.py' -q
.venv/bin/python code/check_artifact.py --forbid-drafts --require-cname \
  --expected-domain "$(cat content/pages/CNAME)" --allow-config-url-mismatch
.venv/bin/python code/check_links.py
```

The link checker requires all local references to resolve.

For the browser suite:

```sh
cd code
npm ci
npx playwright install chromium
npm run check:visual
```

It tests desktop, tablet and mobile layouts, both colour modes, saved theme preferences, Markdown and `llms.txt` endpoints, local resources and horizontal overflow.

## Staging and production

This checkout has two remotes:

| Target | Remote | Local branch | Deployed branch | Domain |
|---|---|---|---|---|
| Production | `production` | `main` | `main` | `seanblanchfield.com` |
| Staging | `staging` | `staging` | `main` | `staging.seanblanchfield.com` |

Each branch must contain the matching domain in `content/pages/CNAME`. The branches normally differ only in that file. Check before every push:

```sh
git branch -vv
cat content/pages/CNAME
git status --short
```

GitHub Actions reads `content/pages/CNAME`, builds with that canonical domain, validates the output, and deploys `site/` to GitHub Pages.

Push only after Sean explicitly authorises that deployment in the current conversation:

```sh
# Staging
git switch staging
git push staging staging:main

# Production
git switch main
git push production main
```

All Git traffic uses the configured Jentic Mini broker remotes. Do not replace them with direct GitHub URLs.

The local tags `pre-python-production-2026-10-22` and `pre-python-staging-2026-10-22` mark the last deployed Jekyll commits for recovery.

## Publishing safeguards

- Never push or publish without Sean's current, explicit authorisation.
- Public staging is still public. Check drafts and source material for sensitive information.
- Stage named files rather than using `git add -A`; local `AGENTS.md` must remain untracked.
- Verify the workflow completed successfully and then fetch the changed public URLs.
- Keep the production and staging `CNAME` values separate.
