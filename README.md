# Python blog prototype

This is a **standalone copy** of the blog content and a small static generator. The existing Jekyll repository at `/workspace/blog/seanblanchfield.com/` is unchanged. The Python version has no Jekyll/Ruby dependency, but it is not yet a verified drop-in replacement. Do not push or deploy without Sean's explicit permission.

## Structure

```text
python-version/seanblanchfield.com/
├── content/
│   ├── posts/               # Edit or add dated Markdown articles here
│   ├── pages/               # Edit about.md, working-with-me.md and settings here
│   ├── assets/              # Source assets
│   └── images/              # Source images
├── code/                    # Generator, CSS, JavaScript and tests
├── site/                    # Generated static output
├── .build-cache/            # Local rendered-content and thumbnail cache
├── screenshots/             # Browser checks; generated
└── README.md
```

Add a post as `content/posts/YYYY-MM-DD-title.md` with YAML front matter, for example:

```markdown
---
title: "An example"
date: 2026-10-19 12:00:00 +0100
image: /images/2026/10/example.jpg
---

Write the post here.
```

The generator produces extensionless `/YYYY/MM/title` HTML and an adjacent `.md` file. The `date` and optional `slug` or `permalink` in front matter control the URL. Save referenced pictures under `content/images/`. The 95 copied source Markdown files contain 94 usable posts; `posts/2022_ezviz_db1_related_posts.md` has no front matter or dated filename and is ignored with a warning. The copy is a snapshot: editing the original Jekyll checkout does not automatically change this tree. Once you adopt this structure, edit here, and avoid maintaining two independent sources of truth.

## Build and preview

Python 3.11 or later. From `/workspace/blog`:

```sh
python3 -m venv python-version/seanblanchfield.com/.venv
python-version/seanblanchfield.com/.venv/bin/python -m pip install -r python-version/seanblanchfield.com/code/requirements.txt
python-version/seanblanchfield.com/.venv/bin/python python-version/seanblanchfield.com/code/build.py --fail-on-drafts
python-version/seanblanchfield.com/.venv/bin/python python-version/seanblanchfield.com/code/preview.py --bind 0.0.0.0 --port 8765
```

Preview **http://preview.home.seanblanchfield.com/** (HTTP redirects to HTTPS). Do not run another server on port 8765: stop the old prototype preview before switching. The preview process serves `site/`, not `content/`; rebuild after an edit and refresh. For fast local edits, add `--incremental`: it reuses rendered Markdown and content-addressed thumbnails from `.build-cache/`, updates files atomically, and removes stale generator-owned outputs. A normal build remains the clean correctness baseline and recreates `site/`; it also reuses the thumbnail cache. The preview has no authentication of its own. Posts marked `draft: true` are built at direct URLs in a non-public build, so restrict the proxy; use `--fail-on-drafts` before public exposure. Sean must review posts at the preview URL before any publication.

Run checks after building:

```sh
python-version/seanblanchfield.com/.venv/bin/python -m unittest discover -s python-version/seanblanchfield.com/code -p 'test_*.py' -q
python-version/seanblanchfield.com/.venv/bin/python python-version/seanblanchfield.com/code/check_artifact.py --forbid-drafts
python-version/seanblanchfield.com/.venv/bin/python python-version/seanblanchfield.com/code/check_links.py --allow-known-source-errors
```

`code/package.json` pins Playwright for the optional twelve-screenshot browser check (`cd code && npm ci && npx playwright install chromium && npm run check:visual`); its browser is a development dependency, not part of a static build. The existing `/workspace/blog/blog-prototype/` environment can also run this check by setting `PLAYWRIGHT_MODULE=/workspace/blog/blog-prototype/node_modules/playwright` and `PLAYWRIGHT_BROWSERS_PATH=/workspace/blog/blog-prototype/.browsers`.

## Differences from Jekyll

All 94 renderable posts appear in **one reverse-chronological homepage**, across `/page/2/`, `/page/3/` and `/page/4/`. There is no `/archive/` listing and no Archive navigation link. Older article URLs are unchanged. The renderer now handles `~~strikethrough~~` and bullet lists immediately after paragraphs, including the list under “Meeting Time” on Working with Me. It copies source assets, produces a feed, HTML/Markdown article pairs and `llms.txt`. Four malformed links inherited from source still need correction; the optional link check allows *only* those four. Labelled fenced code blocks (for example, ` ```bash `, ` ```yaml `, ` ```python ` and ` ```actionscript ` without the spaces) receive build-time syntax highlighting via pinned Pygments 2.19.2; unlabelled or unknown languages remain plain, with no guessing or client-side highlighting script. `code/pygments.css` contains light and dark token colours and is included in the generated `site/assets/css/site.css`. The copied post sources have been audited: all nine previously unlabelled opening fences now specify `systemd` for service units or `text` for logs, output, and iptables rule listings. Three ActionScript-labelled trace-output blocks were also corrected to `text`. Posts with existing `bash`, `yaml`, `python`, and other accurate labels were left alone. These source label changes also appear in the per-article `.md`; Pygments adds colours only to HTML. A short Bash command may have no coloured tokens even when labelled. Full Jekyll/Liquid parity, deployment domain settings and CI still need review. `code/check_artifact.py` can verify a chosen domain when one is agreed. This directory does not contain a `CNAME` because the original checkout currently has a staging CNAME and a production `_config.yml` URL; a deployment must make an explicit domain decision.

### Card thumbnails

The build generates a small WebP thumbnail for every post, page and clipping hero image under `site/images/_cards/`, preserving source subdirectories to prevent duplicate filenames from colliding. Listing pages (homepage, any `/page/N/`, `/clippings/`) reference these ~10–100 KB thumbs instead of each article's full-size hero. Article pages still link the original images. Content-addressed copies in `.build-cache/thumbnails/` mean clean and incremental builds only encode a thumbnail when its source or image settings change. Pillow 13.0 is required (installed via `code/requirements.txt`).

Source images are stored at web-appropriate sizes: photos and artwork now top out at 2000 px on the long edge (quality 82–85 progressive JPEG), gallery full-size images at 3200 px quality 82 (ShipItCon gallery scaled from ~7000 px originals, which remain in the Jekyll checkout's own image folder). Screenshots and diagrams with fine text stay PNG because JPEG artefacts would smear them. Card thumbnails remain WebP generated at build time into `site/images/_cards/`; every listing page loads the small WebP instead of the hero. Total image payload for the homepage was cut from ~30 MB to ~1.3 MB, clippings from ~3.3 MB to ~0.9 MB.

### Delisted posts

A post with `hidden: true` in its front matter stays published at its existing URL (as HTML and Markdown) but leaves the homepage, pagination, feed and the `## Posts` section of `llms.txt`; `llms.txt` lists it under a `## Delisted` heading instead. Seven posts are currently delisted this way (the three Boxee Box pieces, the O2 roaming overcharge, "I'm a complainer", the driving-lessons post and the Ubuntu Natty Narwhal rant) because they are too trivial for the blog now. Delisting is reversible by removing the flag and rebuilding.

### Clippings

Clippings differ from posts: each lives at `content/clippings/YYYY-MM-DD-slug.md` with `link`, `image`, `date`, `source` and `type` front matter, and is displayed on `/clippings/` rather than having its own page. The whole description and an external link to the original source are rendered on the Clippings page; nothing links inside the site, so there is no per-clipping permalink. Thumbnail-style images are sized to fit card layout. To add one, drop a new `content/clippings/*.md` file and rebuild.
