#!/usr/bin/env python3
"""Small, isolated Jekyll-source to static-site prototype (not a Jekyll clone)."""
import argparse
import datetime as dt
import hashlib
import html
import math
import json
import os
import re
import shutil
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

import markdown
from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagInlineProcessor
from markdown.extensions.codehilite import CodeHiliteExtension
import yaml

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
CONTENT = PROJECT / 'content'
CACHE_DIR = PROJECT / '.build-cache'
CACHE_VERSION = 1


class Strikethrough(Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(SimpleTagInlineProcessor(r'(?<!~)(~~)(?!~)(.+?)(?<!~)~~(?!~)', 'del'), 'strikethrough', 55)


def normalize_lists(body):
    """Allow a bullet list immediately after prose, as in the existing pages."""
    lines = body.splitlines(keepends=True)
    result = []
    fenced = False
    for line in lines:
        if re.match(r'^\s*(```|~~~)', line):
            fenced = not fenced
        if (not fenced and re.match(r'^\s{0,3}[-*+]\s+', line) and result
                and result[-1].strip() and not re.match(r'^\s{0,3}[-*+]\s+', result[-1])
                and not re.match(r'^\s*<', result[-1])):
            result.append('\n')
        result.append(line)
    return ''.join(result)
EXCERPT = re.compile(r'<!--\s*more\s*-->', re.IGNORECASE)
POST_NAME = re.compile(r'^\d{4}-\d{2}-\d{2}-(.+)\.(?:md|markdown)$')
LINK_TAG = re.compile(r'{%\s*link\s+([^%]+?)\s*%}')
ATTRS = re.compile(r'(<(?:img|blockquote|p)\b[^>]*>)(?:\s*)\{:([^}]*)\}')
LINKS = {}


@dataclass
class Document:
    source: Path
    data: dict
    body: str
    url: str
    date: dt.datetime | None = None

    @property
    def title(self):
        # Undated clipping filenames are meaningful; dated ones (YYYY-MM-DD-slug)
        # read better as human titles, unless front matter supplies one.
        value = self.data.get('title')
        if value:
            return str(value)
        if self.data.get('layout') == 'clipping':
            stem = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', self.source.stem)
            stem = re.sub(r'-(nuture|nurture)$', '', stem)  # no-op guard; title comes from front matter
            return stem.replace('-', ' ')
        return str(self.source.stem)

    @property
    def draft(self):
        return self.data.get('draft') is True

    @property
    def hidden(self):
        return bool(self.data.get('hidden'))


def load_frontmatter(path):
    text = path.read_text(encoding='utf-8-sig')
    if not text.startswith('---\n'):
        return None
    parts = text.split('\n---', 1)
    if len(parts) != 2:
        raise ValueError(f'Unclosed front matter: {path}')
    data = yaml.safe_load(parts[0][4:]) or {}
    if not isinstance(data, dict):
        raise ValueError(f'Invalid front matter: {path}')
    return data, parts[1].lstrip('\r\n')


def parse_date(value, filename):
    if isinstance(value, dt.datetime):
        return value
    if isinstance(value, dt.date):
        return dt.datetime.combine(value, dt.time())
    if value is None:
        return dt.datetime.strptime(filename[:10], '%Y-%m-%d')
    value = str(value).strip()
    # datetime.fromisoformat also accepts ISO timezone offsets with or without a colon.
    return dt.datetime.fromisoformat(value.replace('Z', '+00:00'))


def post_url(data, date, filename):
    # Jekyll's :year/:month use post.date; :title prefers front-matter slug.
    stem = POST_NAME.match(filename)
    if not stem:
        raise ValueError(f'Unrecognised post filename: {filename}')
    slug = str(data.get('slug') or stem.group(1)).strip()
    slug = re.sub(r'\s+', '-', slug)
    slug = re.sub(r'[^\w.~-]', '', slug, flags=re.UNICODE)
    if not slug or slug in ('.', '..'):
        raise ValueError(f'Invalid slug: {filename}')
    return str(data.get('permalink') or f'/{date:%Y/%m}/{slug}')


def output_path(out, url):
    path = urlsplit(url).path
    if not path.startswith('/') or '\\' in path or any(p in ('.', '..') for p in path.split('/')):
        raise ValueError(f'Unsafe URL: {url}')
    path = path.lstrip('/')
    if not path or path.endswith('/'):
        path += 'index.html'
    elif Path(path).suffix not in ('.html', '.xml', '.txt', '.md', '.ico'):
        path += '.html'
    target = out / path
    if not target.resolve().is_relative_to(out.resolve()):
        raise ValueError(f'Unsafe output: {url}')
    return target


def atomic_write(target, content, binary=False):
    """Replace one output atomically, avoiding needless writes."""
    payload = content if binary else content.encode('utf-8')
    if target.is_file() and target.read_bytes() == payload:
        return False
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=target.parent, prefix=f'.{target.name}.', delete=False) as handle:
        temp = Path(handle.name)
        try:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        except Exception:
            temp.unlink(missing_ok=True)
            raise
    os.replace(temp, target)
    return True


def save(out, url, content, written):
    target = output_path(out, url)
    if target in written:
        raise ValueError(f'Duplicate output path: {target}')
    atomic_write(target, content)
    written.add(target)


def digest_bytes(content):
    return hashlib.blake2b(content, digest_size=20).hexdigest()


def file_fingerprint(path):
    return digest_bytes(path.read_bytes())


def load_cache(cache_dir, fingerprint):
    manifest = cache_dir / 'manifest.json'
    try:
        data = json.loads(manifest.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return {'version': CACHE_VERSION, 'fingerprint': fingerprint, 'documents': {}, 'outputs': []}
    if data.get('version') != CACHE_VERSION or data.get('fingerprint') != fingerprint:
        return {'version': CACHE_VERSION, 'fingerprint': fingerprint, 'documents': {}, 'outputs': []}
    data.setdefault('documents', {})
    data.setdefault('outputs', [])
    return data


def save_cache(cache_dir, data):
    cache_dir.mkdir(parents=True, exist_ok=True)
    atomic_write(cache_dir / 'manifest.json', json.dumps(data, ensure_ascii=False, sort_keys=True))


def remove_stale_outputs(out, old_outputs, desired_outputs):
    """Remove obsolete generator-owned files after a successful incremental build."""
    for relative in sorted(set(old_outputs) - set(desired_outputs), reverse=True):
        target = (out / relative).resolve()
        if target.is_relative_to(out) and target.is_file() and not target.is_symlink():
            target.unlink()
            parent = target.parent
            while parent != out:
                try:
                    parent.rmdir()
                except OSError:
                    break
                parent = parent.parent


# Card thumbnails cap card art at realistic display size (nearest 2x-DPI step)
CARD_WIDTH = 800
THUMB_DIR_NAME = '_cards'
try:
    from PIL import Image  # Pillow is only required when copying images.
except ImportError:  # pragma: no cover - build works without image rewriting
    Image = None

def card_thumb_url(image_path):
    """Map an image URL to a collision-free generated thumbnail URL."""
    path = urlsplit(str(image_path)).path
    if not path.startswith('/images/'):
        raise ValueError(f'Card image must be under /images/: {image_path}')
    relative = Path(path[len('/images/'):])
    if not relative.name or any(part in ('.', '..') for part in relative.parts):
        raise ValueError(f'Unsafe card image path: {image_path}')
    return '/' + (Path('images') / THUMB_DIR_NAME / relative.with_suffix('.webp')).as_posix()


def generate_card_thumbnails(source, out, jobs, cache_dir):
    """Reuse content-addressed WebP card thumbnails across clean builds."""
    if Image is None:
        print('Pillow not installed; card thumbnails skipped', file=sys.stderr)
        return set()
    generated = set()
    thumb_cache = cache_dir / 'thumbnails'
    thumb_cache.mkdir(parents=True, exist_ok=True)
    for url, _source_path in jobs:
        src = source / url.lstrip('/')
        if not src.is_file():
            continue
        relative = card_thumb_url(url).lstrip('/')
        dest = out / relative
        key = digest_bytes(src.read_bytes() + f'|{CARD_WIDTH}|78|6|{getattr(Image, "__version__", "")}'.encode())
        cached = thumb_cache / f'{key}.webp'
        try:
            if not cached.is_file():
                cached.parent.mkdir(parents=True, exist_ok=True)
                with Image.open(src) as img:
                    rgb = img.convert('RGB')
                    rgb.thumbnail((CARD_WIDTH, CARD_WIDTH * 4))
                    with tempfile.NamedTemporaryFile(dir=cached.parent, suffix='.webp', delete=False) as handle:
                        temp = Path(handle.name)
                    try:
                        rgb.save(temp, 'WEBP', quality=78, method=6)
                        os.replace(temp, cached)
                    finally:
                        temp.unlink(missing_ok=True)
            atomic_write(dest, cached.read_bytes(), binary=True)
            generated.add(relative)
        except OSError as exc:
            print(f'Card thumbnail skipped for {src.name}: {exc}', file=sys.stderr)
    return generated


def caption_images(markup):
    """Turn the source site's captioned image marker into an accessible figure."""
    pattern = re.compile(r'<p>\s*(<img\b[^>]*\bclass="[^"]*\bcaptioned\b[^"]*"[^>]*\/?>)(.*?)</p>', re.DOTALL)
    def replace(match):
        tag = match.group(1)
        alt_match = re.search(r'\balt="([^"]*)"', tag)
        classes_match = re.search(r'\bclass="([^"]*)"', tag)
        caption = alt_match.group(1) if alt_match else ''
        classes = classes_match.group(1) if classes_match else 'captioned'
        trailing = match.group(2).strip()
        # Only promote a standalone image; keep prose that follows an image in the same paragraph.
        if trailing:
            return match.group(0)
        return (f'<figure class="{classes}">{tag}'
                + (f'<figcaption>{caption}</figcaption>' if caption else '') + '</figure>')
    return pattern.sub(replace, markup)


def portable_markdown(body):
    """Resolve Jekyll post links in both HTML input and LLM-readable Markdown."""
    def resolve_link(match):
        path = match.group(1).strip().lstrip('/')
        if path not in LINKS:
            raise ValueError(f'Unresolved Jekyll link: {path}')
        return LINKS[path]
    body = LINK_TAG.sub(resolve_link, body)
    # Only the Liquid wrappers are removed. Home Assistant/Jinja examples inside remain literal.
    return re.sub(r'{%\s*(?:raw|endraw)\s*%}', '', body)


def split_excerpt(body):
    """Accept the spaced and unspaced Jekyll excerpt markers."""
    return EXCERPT.split(body, maxsplit=1)[0]


def render_markdown(body):
    # Do NOT evaluate Liquid/Jinja in source text: Home Assistant examples use it.
    result = markdown.markdown(normalize_lists(portable_markdown(body)), extensions=[
        'fenced_code', 'tables', 'sane_lists', 'toc', 'attr_list', Strikethrough(),
        CodeHiliteExtension(guess_lang=False, css_class='codehilite', use_pygments=True)])
    def apply_attrs(match):
        classes = re.findall(r'\.([\w-]+)', match.group(2))
        return match.group(1)[:-1] + (' class="' + ' '.join(classes) + '"' if classes else '') + '>'
    return caption_images(ATTRS.sub(apply_attrs, result))


def plain_text(markup):
    """Normalize rendered markup into metadata-safe readable text."""
    text = html.unescape(re.sub(r'<[^>]+>', ' ', markup))
    return re.sub(r'\s+', ' ', text).strip()


def meta_description(description, body='', limit=160):
    """Return a non-empty, word-safe description no longer than limit."""
    text = plain_text(description) if description else plain_text(render_markdown(split_excerpt(body)))
    if len(text) <= limit:
        return text
    shortened = text[:limit + 1].rsplit(' ', 1)[0].rstrip(' ,;:-')
    return (shortened or text[:limit]).rstrip() + '…'


def page(title, body, site_title, url, description='', image=None, draft=False, date=None,
         layout='page', author=None, modified_date=None, base='https://seanblanchfield.com',
         site_description='Essays on tech, business and how things work', redirect_to=None,
         schema_type=None):
    esc = html.escape
    canonical_raw = base.rstrip('/') + url
    canonical = esc(canonical_raw, quote=True)
    description = meta_description(description, body) or site_description
    markdown_link = bool(date)
    authors = ([author] if isinstance(author, str) else list(author or [])) if date else []
    authors = [str(name) for name in authors if name] or (['Sean Blanchfield'] if date else [])
    image_url = str(image or '')
    if image_url.startswith('/'):
        image_url = base.rstrip('/') + image_url
    seo = (f'<link rel="canonical" href="{canonical}">'
           f'<meta property="og:title" content="{esc(title, quote=True)}">'
           f'<meta property="og:type" content="{"article" if date else "website"}">'
           f'<meta property="og:url" content="{canonical}">'
           f'<meta property="og:site_name" content="{esc(site_title, quote=True)}">'
           f'<meta property="og:description" content="{esc(description, quote=True)}">'
           f'<meta name="twitter:card" content="{"summary_large_image" if image else "summary"}">'
           f'<meta name="twitter:title" content="{esc(title, quote=True)}">'
           f'<meta name="twitter:description" content="{esc(description, quote=True)}">')
    if image_url:
        seo += (f'<meta property="og:image" content="{esc(image_url, quote=True)}">'
                f'<meta name="twitter:image" content="{esc(image_url, quote=True)}">')
    if date:
        published_iso = date.isoformat()
        modified = parse_date(modified_date, '') if modified_date else date
        seo += (f'<meta property="article:published_time" content="{esc(published_iso, quote=True)}">'
                f'<meta property="article:modified_time" content="{esc(modified.isoformat(), quote=True)}">')
    if draft or url == '/404.html':
        seo += '<meta name="robots" content="noindex,nofollow">'
    alternate = (f'<link rel="alternate" type="text/markdown" href="{esc(canonical_raw, quote=True)}.md">'
                 if markdown_link else '')
    if date:
        schema = {
            '@context': 'https://schema.org', '@type': 'BlogPosting',
            'headline': title, 'description': description, 'url': canonical_raw,
            'mainEntityOfPage': {'@type': 'WebPage', '@id': canonical_raw},
            'datePublished': date.isoformat(), 'dateModified': modified.isoformat(),
            'author': [{'@type': 'Person', 'name': name,
                        'url': base.rstrip('/') + '/about/'} for name in authors],
            'publisher': {'@type': 'Person', 'name': 'Sean Blanchfield',
                          'url': base.rstrip('/') + '/about/'},
        }
        if image_url:
            schema['image'] = image_url
    else:
        page_type = schema_type or ('AboutPage' if url == '/about/' else
                                    'CollectionPage' if layout == 'index' else 'WebPage')
        schema = {'@context': 'https://schema.org', '@type': page_type,
                  'name': title, 'description': description, 'url': canonical_raw,
                  'isPartOf': {'@type': 'WebSite', 'name': site_title,
                               'url': base.rstrip('/') + '/'}}
        if url == '/about/':
            schema['mainEntity'] = {
                '@type': 'Person', 'name': 'Sean Blanchfield', 'url': canonical_raw,
                'image': image_url or None,
                'sameAs': ['https://github.com/seanblanchfield',
                           'https://www.linkedin.com/in/seanblanchfield',
                           'https://x.com/seanblanchfield']}
            schema['mainEntity'] = {key: value for key, value in schema['mainEntity'].items() if value}
    structured = '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + '</script>'
    if date:
        meta = f'<time class="dt-published" datetime="{date.isoformat()}" itemprop="datePublished">{date:%-d %b %Y}</time>'
        if modified_date:
            meta += f' <span aria-hidden="true">·</span> Updated <time class="dt-modified" datetime="{modified.isoformat()}" itemprop="dateModified">{modified:%-d %b %Y}</time>'
        meta += (' <span aria-hidden="true">·</span> '
                 f'<span itemprop="author" itemscope itemtype="https://schema.org/Person">'
                 f'<span itemprop="name">{esc(", ".join(authors))}</span></span>')
        meta += f' <span aria-hidden="true">·</span> <a class="markdown-link" href="{esc(url, quote=True)}.md">Markdown</a>'
        hero_image = (f'<img src="{esc(str(image), quote=True)}" alt="">' if image else '')
        badge = ' <span class="draft-badge">Draft</span>' if draft else ''
        content = (f'<article class="post h-entry" itemscope itemtype="https://schema.org/BlogPosting">'
                   f'<div class="article-hero">{hero_image}'
                   f'<div class="article-hero__text"><h1 class="p-name" itemprop="headline">{esc(title)}{badge}</h1>'
                   f'<p class="article-hero__meta">{meta}</p></div></div>'
                   f'<div class="article-body e-content" itemprop="articleBody">{body}</div>'
                   f'<a class="u-url" href="{esc(url, quote=True)}" hidden></a></article>')
    elif layout == 'index':
        content = body
    elif redirect_to:
        target = esc(redirect_to, quote=True)
        content = (f'<meta http-equiv="refresh" content="0;url={target}">'
                   f'<link rel="canonical" href="{esc(base + redirect_to, quote=True)}">'
                   f'<article class="static-page"><h1>{esc(title)}</h1>{body}'
                   f'<p><a href="{target}">{target}</a></p></article>')
    else:
        hero_image = f'<img class="page-hero" src="{esc(str(image), quote=True)}" alt="">' if image else ''
        content = f'<article class="static-page"><h1>{esc(title)}</h1>{hero_image}{body}</article>'
    footer = (f'<a href="{esc(url, quote=True)}.md">This article as Markdown</a> <span aria-hidden="true">·</span> '
              if markdown_link else '')
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{esc(title)} · {esc(site_title)}</title>'
            f'<meta name="description" content="{esc(description, quote=True)}">'
            f'{seo}{structured}<link rel="stylesheet" href="/assets/css/site.css">'
            f'<link rel="icon" href="/assets/favicon.ico">'
            f'<link rel="alternate" type="application/atom+xml" href="/feed.xml">'
            f'<link rel="alternate" type="text/plain" href="/llms.txt" title="LLM-readable site index">'
            f'{alternate}</head><body><a class="skip-link" href="#main-content">Skip to content</a>'
            f'<header class="site-header"><div class="shell masthead">'
            f'<div class="site-description"><a class="site-title" href="/">'
            f'<span class="site-title__dot" aria-hidden="true"></span>{esc(site_title)}</a>'
            f'<p class="site-tagline">{esc(site_description)}</p></div>'
            f'<div class="header-actions">'
            f'<div class="header-tools"><nav class="social-links" aria-label="Social profiles">'
            f'<a href="https://github.com/seanblanchfield" rel="me" aria-label="GitHub" title="GitHub">'
            f'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 .7a11.5 11.5 0 0 0-3.6 22.4c.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.4-4-1.4-.5-1.4-1.3-1.8-1.3-1.8-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.7 1.3 3.4 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.5.1-3.1 0 0 1-.3 3.3 1.2a11.4 11.4 0 0 1 6 0C17 4.7 18 5 18 5c.6 1.6.2 2.8.1 3.1.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.2c0 .3.2.7.8.6A11.5 11.5 0 0 0 12 .7Z"/></svg></a>'
            f'<a href="https://www.linkedin.com/in/seanblanchfield" rel="me" aria-label="LinkedIn" title="LinkedIn">'
            f'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M5.3 7.8H1.7V22h3.6V7.8ZM3.5 2A2.1 2.1 0 1 0 3.5 6.2 2.1 2.1 0 0 0 3.5 2ZM22.3 13.9c0-4.3-2.3-6.3-5.4-6.3-2.5 0-3.6 1.4-4.2 2.3V7.8H9.1V22h3.6v-7c0-1.9.4-3.7 2.7-3.7 2.3 0 2.3 2.1 2.3 3.8V22h3.6l1-8.1Z"/></svg></a>'
            f'<a href="https://x.com/seanblanchfield" rel="me" aria-label="X" title="X">'
            f'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M18.9 2h3.7l-8.1 9.2L24 22h-7.4l-5.8-7.6L4.1 22H.4l8.7-9.9L0 2h7.6l5.2 6.9L18.9 2Zm-1.3 18.1h2L6.5 3.8H4.3l13.3 16.3Z"/></svg></a>'
            f'</nav>'
            f'<button id="theme-toggle" class="theme-toggle" type="button" role="switch" aria-label="Dark mode" aria-checked="false" title="Dark mode">'
            f'<span class="theme-toggle__track" aria-hidden="true"><span class="theme-toggle__thumb">'
            f'<svg class="theme-toggle__sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="3.8"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M4.9 4.9l1.4 1.4m11.4 11.4 1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4"/></svg>'
            f'<svg class="theme-toggle__moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 15.6A8.8 8.8 0 0 1 8.4 3.5 8.8 8.8 0 1 0 20.5 15.6Z"/></svg>'
            f'</span></span></button></div>'
            f'<nav class="site-nav" aria-label="Main navigation">'
            f'<a href="/about/">Bio</a>'
            f'<a href="/clippings/">Clippings</a></nav>'
            f'</div></div></header>'
            f'<main id="main-content" class="{layout}-main">{content}</main>'
            f'<footer class="site-footer"><div class="shell">{footer}'
            f'<a href="/feed.xml">RSS</a> <span aria-hidden="true">·</span> '
            f'<a href="/llms.txt">llms.txt</a></div></footer>'
            f'<script src="/assets/js/theme.js" defer></script></body></html>\n')


def post_excerpt(post, words):
    text = getattr(post, '_excerpt_text', None)
    if text is None:
        text = plain_text(render_markdown(split_excerpt(post.body)))
    parts = text.split(' ')
    return html.escape(' '.join(parts[:words]) + ('…' if len(parts) > words else ''))


def card_image(post, class_name):
    # No external image dependencies; cards without a hero use the navy fallback.
    # Cards show a generated small WebP (card_thumb_url) so listing pages do not
    # download multi-megabyte hero files just to draw a 380px thumbnail.
    image = post.data.get('image')
    if not image:
        return f'<div class="{class_name}" aria-hidden="true"></div>'
    src = card_thumb_url(str(image))
    return (f'<div class="{class_name}"><img src="{html.escape(src, quote=True)}"'
            f' alt="" loading="lazy"></div>')


def index_page(title, posts, site_title, desc, prefix='/', page_number=1, pages=1, section='/', base='https://seanblanchfield.com'):
    esc = html.escape
    def card(post):
        href = esc(post.url, quote=True)
        return (f'<li class="post-card"><a class="post-card__image-link" href="{href}" aria-label="{esc(post.title, quote=True)}">'
                f'{card_image(post, "post-card__image")}</a><div class="post-card__body">'
                f'<time datetime="{post.date.date().isoformat()}">{post.date:%-d %b %Y}</time>'
                f'<h3><a href="{href}">{esc(post.title)}</a></h3>'
                f'<p>{post_excerpt(post, 28)}</p><a class="card-cta" href="{href}">Read &rarr;</a></div></li>')
    def mini(post):
        href = esc(post.url, quote=True)
        return (f'<li class="mini-card"><a href="{href}">{card_image(post, "mini-card__image")}'
                f'<span class="mini-card__body"><time datetime="{post.date.date().isoformat()}">{post.date:%-d %b %Y}</time>'
                f'<span class="mini-card__title">{esc(post.title)}</span></span></a></li>')
    body = ''
    if section == '/' and page_number == 1 and posts:
        lead = posts[0]
        href = esc(lead.url, quote=True)
        body += (f'<section class="feature-lead" aria-label="Featured essay">'
                 f'<a class="feature-lead__image-link" href="{href}" aria-label="{esc(lead.title, quote=True)}">'
                 f'{card_image(lead, "feature-lead__image")}</a><div class="feature-lead__body">'
                 f'<time datetime="{lead.date.date().isoformat()}">{lead.date:%-d %b %Y}</time>'
                 f'<h1><a href="{href}">{esc(lead.title)}</a></h1>'
                 f'<p>{post_excerpt(lead, 45)}</p><a class="card-cta" href="{href}">Read the essay &rarr;</a>'
                 f'</div></section><div class="section-divider"><span>More writing</span></div>')
        posts = posts[1:]
        body += '<ul class="post-grid">' + ''.join(card(post) for post in posts[:8]) + '</ul>'
        if posts[8:]:
            body += '<ul class="mini-grid">' + ''.join(mini(post) for post in posts[8:]) + '</ul>'
    else:
        body += f'<h1 class="listing-heading">{esc(title if page_number == 1 else f"{title} · Page {page_number}")}</h1>'
        body += '<ul class="post-grid">' + ''.join(card(post) for post in posts) + '</ul>'
    previous = section if page_number == 2 else f'{section}page/{page_number-1}/'
    newer = f'<a href="{previous}">&larr; Newer</a>' if page_number > 1 else ''
    older = f'<a href="{section}page/{page_number+1}/">Older &rarr;</a>' if page_number < pages else ''
    if newer or older:
        body += f'<nav class="pager" aria-label="Pagination">{newer}{older}</nav>'
    return page(title, f'<div class="shell listing">{body}</div>', site_title, prefix, desc, layout='index', base=base, site_description=desc)


def clippings_page(entries, site_title, base='https://seanblanchfield.com'):
    esc = html.escape
    def card(entry):
        # Clippings are display-only: the whole story stays on the page, so the
        # title and body are NOT links and the card carries no CTA.
        link = esc(str(entry.data.get('link') or ''), quote=True)
        body_html = getattr(entry, '_body_html', None) or render_markdown(entry.body)
        image_html = (f'<img src="{esc(card_thumb_url(str(entry.data["image"])), quote=True)}" alt="" loading="lazy">'
                      if entry.data.get('image') else '')
        return (f'<li class="clipping-card"><div class="clipping-card__image">{image_html}</div>'
                f'<div class="clipping-card__body">'
                f'<time datetime="{entry.date.date().isoformat()}">{entry.date:%-d %b %Y}</time>'
                f'<h3>{esc(entry.title)}</h3>'
                f'<p class="clipping-card__source">{esc(str(entry.data.get("source") or ""))}</p>'
                f'{body_html}'
                f'<a class="clipping-card__link" href="{link}">{link}</a>'
                f'</div></li>')
    head = '<p class="clipping-card__intro">Press, pods and interviews featuring Sean.</p>'
    body = f'<h1 class="listing-heading">Clippings</h1>{head}<ul class="clipping-list">' + ''.join(card(e) for e in entries) + '</ul>'
    return page('Clippings', f'<div class="shell listing">{body}</div>', site_title, '/clippings/', 'Press, podcasts and interviews',
                layout='index', base=base, site_description='Essays on tech, business and how things work')


def utc_iso(value):
    """Atom accepts ISO-8601 timestamps; normalize naive source dates to UTC."""
    if value.tzinfo is None:
        value = value.replace(tzinfo=dt.timezone.utc)
    return value.astimezone(dt.timezone.utc).isoformat().replace('+00:00', 'Z')


def atom_feed(posts, base, title, description):
    atom = 'http://www.w3.org/2005/Atom'
    ET.register_namespace('', atom)
    E = lambda name, **attrs: ET.Element(f'{{{atom}}}{name}', attrs)
    root = E('feed')
    ET.SubElement(root, f'{{{atom}}}title').text = title
    ET.SubElement(root, f'{{{atom}}}subtitle').text = description
    ET.SubElement(root, f'{{{atom}}}id').text = base + '/'
    ET.SubElement(root, f'{{{atom}}}link', {'href': base + '/feed.xml', 'rel': 'self',
                                           'type': 'application/atom+xml'})
    ET.SubElement(root, f'{{{atom}}}link', {'href': base + '/', 'rel': 'alternate',
                                           'type': 'text/html'})
    author = ET.SubElement(root, f'{{{atom}}}author')
    ET.SubElement(author, f'{{{atom}}}name').text = 'Sean Blanchfield'
    ET.SubElement(author, f'{{{atom}}}uri').text = base + '/about/'
    updated_dates = [parse_date(p.data.get('modified_date'), '') if p.data.get('modified_date') else p.date
                     for p in posts]
    latest = max(updated_dates, key=lambda value: value.replace(tzinfo=None)) if updated_dates else dt.datetime(1970, 1, 1)
    ET.SubElement(root, f'{{{atom}}}updated').text = utc_iso(latest)
    for post in posts[:20]:
        entry = ET.SubElement(root, f'{{{atom}}}entry')
        ET.SubElement(entry, f'{{{atom}}}title').text = post.title
        ET.SubElement(entry, f'{{{atom}}}id').text = base + post.url
        ET.SubElement(entry, f'{{{atom}}}link', {'href': base + post.url, 'rel': 'alternate',
                                                 'type': 'text/html'})
        ET.SubElement(entry, f'{{{atom}}}link', {'href': base + post.url + '.md', 'rel': 'alternate',
                                                 'type': 'text/markdown'})
        ET.SubElement(entry, f'{{{atom}}}published').text = utc_iso(post.date)
        modified = parse_date(post.data.get('modified_date'), '') if post.data.get('modified_date') else post.date
        ET.SubElement(entry, f'{{{atom}}}updated').text = utc_iso(modified)
        ET.SubElement(entry, f'{{{atom}}}summary', {'type': 'html'}).text = getattr(
            post, '_excerpt_html', None) or render_markdown(split_excerpt(post.body))
    return ET.tostring(root, encoding='unicode', xml_declaration=True) + '\n'


def sitemap_xml(entries, base):
    """Create a standard sitemap of canonical, indexable HTML documents."""
    namespace = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    ET.register_namespace('', namespace)
    root = ET.Element(f'{{{namespace}}}urlset')
    for url, modified in entries:
        node = ET.SubElement(root, f'{{{namespace}}}url')
        ET.SubElement(node, f'{{{namespace}}}loc').text = base + url
        if modified:
            ET.SubElement(node, f'{{{namespace}}}lastmod').text = modified.date().isoformat()
    return ET.tostring(root, encoding='unicode', xml_declaration=True) + '\n'


def build(source=CONTENT, out=PROJECT / 'site', copy_images=True, fail_on_drafts=False,
          site_url=None, incremental=False, cache_dir=CACHE_DIR):  # noqa: C901
    if out.is_symlink():
        raise ValueError('Refusing to overwrite a symlinked output directory')
    source, out = source.resolve(), out.resolve()
    if not source.is_dir() or not (source / 'pages/_config.yml').is_file():
        raise ValueError('--source must contain pages/_config.yml')
    if source != CONTENT or out == source or source.is_relative_to(out):
        raise ValueError('Source must be this project content/ directory, separate from site/')
    if out != PROJECT / 'site':
        raise ValueError('Output must be the generated site/ directory in this project')
    if (out / '.keep').exists():
        raise ValueError('Refusing to overwrite a protected output directory')
    config = yaml.safe_load((source / 'pages/_config.yml').read_text())
    base = str(site_url or config.get('url') or '').rstrip('/')
    cta_path = source / 'pages/llm-cta.md'
    if not cta_path.is_file():
        raise ValueError('Missing content/pages/llm-cta.md')
    llm_cta = cta_path.read_text(encoding='utf-8').strip()
    if not llm_cta:
        raise ValueError('content/pages/llm-cta.md must not be empty')
    llm_cta = llm_cta.replace('https://seanblanchfield.com/feed.xml', base + '/feed.xml')
    parsed_base = urlsplit(base)
    if (parsed_base.scheme != 'https' or not parsed_base.hostname or parsed_base.path or
            parsed_base.query or parsed_base.fragment or parsed_base.username or parsed_base.password):
        raise ValueError('Site URL must be a bare https://domain without a path or credentials')
    title = str(config.get('title') or 'Blog')
    description = str(config.get('description') or '')
    generator_files = [Path(__file__), HERE / 'site.css', HERE / 'pygments.css', HERE / 'theme.js']
    fingerprint = digest_bytes(b''.join(path.read_bytes() for path in generator_files) +
                               json.dumps({'base': base, 'copy_images': copy_images}, sort_keys=True).encode())
    render_fingerprint = digest_bytes(Path(__file__).read_bytes() +
                                      f'{markdown.__version__}|{yaml.__version__}'.encode())
    cache_dir = Path(cache_dir).resolve()
    if cache_dir == out or cache_dir.is_relative_to(out):
        raise ValueError('Build cache must remain outside site/')
    cache = load_cache(cache_dir, fingerprint) if incremental else {
        'version': CACHE_VERSION, 'fingerprint': fingerprint, 'documents': {}, 'outputs': []}
    posts = []
    ignored = []
    for path in sorted(source.glob('posts/*.md')):
        parsed = load_frontmatter(path)
        if parsed is None:
            ignored.append(path)
            continue
        data, body = parsed
        date = parse_date(data.get('date'), path.name)
        url = post_url(data, date, path.name)
        posts.append(Document(path, data, body, url, date))
    drafts = [post for post in posts if post.draft]
    if fail_on_drafts and drafts:
        raise ValueError('Refusing public build with draft: true posts: ' +
                         ', '.join(str(post.source.relative_to(source)) for post in drafts))
    LINKS.clear()
    LINKS.update({f'{section}/_posts/{post.source.name}': post.url for post in posts
                  for section in ('current', 'archive')})
    LINKS.update({f'posts/{post.source.name}': post.url for post in posts})
    link_pages = []
    clipping_source = source / 'clippings'
    if clipping_source.is_dir():
        for path in sorted(clipping_source.glob('*.md')):
            parsed = load_frontmatter(path)
            if parsed is None:
                continue
            data, body = parsed
            if not data.get('link'):
                raise ValueError(f'Clipping missing link: {path}')
            date = parse_date(data.get('date'), path.name)
            link_pages.append(Document(path, data, body, '/clippings/', date))
    link_pages.sort(key=lambda e: e.date.replace(tzinfo=None), reverse=True)
    pages = []
    for path in sorted((source / 'pages').iterdir()):
        if path.name in {'AGENTS.md', 'llm-cta.md'} or path.suffix not in ('.md', '.html'):
            continue
        parsed = load_frontmatter(path)
        if not parsed:
            continue
        data, body = parsed
        if data.get('layout') == 'home':
            continue
        if data.get('draft') is True and fail_on_drafts:
            raise ValueError(f'Refusing public build with draft: true page: {path.relative_to(source)}')
        url = str(data.get('permalink') or ('/404.html' if path.name == '404.html' else f'/{path.stem}/'))
        if url == '/clippings/':
            continue  # Clippings page is generated from content/clippings/, not content/pages/.
        pages.append(Document(path, data, body, url))
    # Clean builds recreate site/, while incremental builds reconcile owned outputs in place.
    if out.exists() and not incremental:
        shutil.rmtree(out)
    out.mkdir(parents=True, exist_ok=True)
    written = set()
    document_cache = cache['documents']

    links_fingerprint = digest_bytes(json.dumps(LINKS, sort_keys=True).encode())

    def rendered(document):
        relative = document.source.relative_to(source).as_posix()
        key = digest_bytes(document.source.read_bytes() + render_fingerprint.encode() + links_fingerprint.encode())
        cached = document_cache.get(relative)
        if cached and cached.get('key') == key:
            return cached['body'], cached['excerpt'], cached['description']
        body_html = render_markdown(document.body)
        excerpt_html = render_markdown(split_excerpt(document.body))
        result = (body_html, excerpt_html,
                  meta_description(document.data.get('description', ''), split_excerpt(document.body)))
        document_cache[relative] = {'key': key, 'body': result[0], 'excerpt': result[1],
                                    'description': result[2]}
        return result
    llms_redirects = []
    for document in posts + pages + link_pages:
        body_html, excerpt_html, cached_description = rendered(document)
        document._body_html = body_html
        document._excerpt_html = excerpt_html
        document._excerpt_text = plain_text(excerpt_html)
        document._description = cached_description
    if link_pages:
        save(out, '/clippings/', clippings_page(link_pages, title, base=base), written)
    for post in posts:
        redirect_target = post.data.get('redirect_to')
        if redirect_target:
            target = str(redirect_target)
            if not target.startswith('/') or target == post.url:
                raise ValueError(f'Invalid redirect_to in {post.source.name}: {redirect_target!r}')
            redir_src = (f'<!doctype html><html><head><meta charset="utf-8">'
                         f'<meta http-equiv="refresh" content="0;url={html.escape(target, quote=True)}">'
                         f'<link rel="canonical" href="{html.escape(base + target, quote=True)}"></head>'
                         f'<body><p>This item has moved to <a href="{html.escape(target, quote=True)}">{html.escape(target, quote=True)}</a>.</p></body></html>\n')
            save(out, post.url, redir_src, written)
            save(out, post.url.rstrip('/') + '.md', f'{llm_cta}\n\n---\n\n# {post.title}\n\nMoved to: {base}{target}\n', written)
            llms_redirects.append((post, target))
            continue
        summary = post._description
        save(out, post.url, page(post.title, post._body_html, title, post.url,
                                 summary, post.data.get('image'), post.draft, post.date,
                                 author=post.data.get('author'),
                                 modified_date=post.data.get('modified_date'),
                                 base=base, site_description=description), written)
        md = (f'{llm_cta}\n\n---\n\n# {post.title}\n\nPublished: {post.date.date().isoformat()}\n'
              f'Canonical: {base}{post.url}\n\n{portable_markdown(post.body)}')
        save(out, post.url + '.md', md, written)
    for document in pages:
        redirect_target = document.data.get('redirect_to')
        if redirect_target:
            target = str(redirect_target)
            if not target.startswith('/') or target == document.url:
                raise ValueError(f'Invalid redirect_to in {document.source.name}: {redirect_target}')
            md_stub = (f'{llm_cta}\n\n---\n\n# How I work\n\nMoved to: {base}{target}\n')
            save(out, document.url, page(document.title, document._body_html, title, document.url,
                                         base=base, site_description=description, redirect_to=target), written)
            save(out, document.url.rstrip('/') + '.md', md_stub, written)
            continue
        body = document._body_html if document.source.suffix == '.md' else document.body
        page_description = document._description
        save(out, document.url, page(document.title, body, title, document.url,
                                     description=page_description, image=document.data.get('image'), base=base,
                                     site_description=description), written)
    listed = sorted((p for p in posts if not (p.draft or p.hidden or p.data.get('redirect_to'))),
                    key=lambda p: p.date.replace(tzinfo=None), reverse=True)
    total = math.ceil(len(listed) / 30)
    index_urls = []
    for n in range(1, total + 1):
        url = '/' if n == 1 else f'/page/{n}/'
        save(out, url, index_page(title, listed[(n-1)*30:n*30], title, description, url, n, total, base=base), written)
        index_urls.append((url, listed[0].date if listed else None))
    save(out, '/feed.xml', atom_feed(listed, base, title, description), written)
    sitemap_entries = list(index_urls)
    sitemap_entries += [(p.url, parse_date(p.data.get('modified_date'), '') if p.data.get('modified_date') else p.date)
                        for p in listed]
    sitemap_entries += [(p.url, None) for p in pages
                        if p.url != '/404.html' and not p.data.get('redirect_to')]
    if link_pages:
        sitemap_entries.append(('/clippings/', max(p.date for p in link_pages)))
    save(out, '/sitemap.xml', sitemap_xml(sitemap_entries, base), written)
    save(out, '/robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n', written)
    llms = f'{llm_cta}\n\n---\n\n# {title}\n\n{description}\n\n## Posts\n\n' + ''.join(
        f'- [{p.title}]({base}{p.url}.md)\n' for p in listed)
    llms += '\n## Pages\n\n' + ''.join(f'- [{p.title}]({base}{p.url})\n' for p in pages if p.url != '/404.html' and not p.data.get('hidden'))
    hidden_posts = [p for p in posts if p.hidden]
    if hidden_posts:
        llms += '\n## Delisted (not linked; kept at these URLs for citation)\n\n' + ''.join(
            f'- [{p.title}]({base}{p.url.rstrip("/")}.md)\n' for p in sorted(hidden_posts, key=lambda p: p.date.replace(tzinfo=None), reverse=True)
            if p.url not in {p.url for p in listed})
    if llms_redirects:
        llms += '\n## Moved to Clippings\n\n' + ''.join(
            f'- [{p.title}]({base}/{target.lstrip("/")})\n'
            for p, target in llms_redirects)
    save(out, '/llms.txt', llms, written)
    for post in posts:
        for redirect in post.data.get('redirect_from') or []:
            if redirect == post.url:
                continue
            target = html.escape(post.url, quote=True)
            redir = f'<!doctype html><html><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;url={target}"><link rel="canonical" href="{html.escape(base + post.url, quote=True)}"></head><body><a href="{target}">Moved</a></body></html>\n'
            save(out, redirect, redir, written)
    asset_outputs = set()
    cname = source / 'pages/CNAME'
    if cname.is_file():
        atomic_write(out / 'CNAME', cname.read_bytes(), binary=True)
        asset_outputs.add('CNAME')
    for name in ('assets', 'images'):
        folder = source / name
        if folder.is_dir() and (name != 'images' or copy_images):
            for src in folder.rglob('*'):
                if (not src.is_file() or src.is_symlink() or src.name == '.DS_Store' or
                        src.name.startswith('._') or any(part in {'.git', '.env'} for part in src.parts)):
                    continue
                relative = src.relative_to(source).as_posix()
                dest = out / relative
                if not (incremental and dest.is_file() and dest.stat().st_size == src.stat().st_size and
                        dest.stat().st_mtime_ns == src.stat().st_mtime_ns):
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dest)
                asset_outputs.add(relative)
    if copy_images:
        hero_jobs = [(str(p.data.get('image')), str(p.source))
                     for p in posts + pages + link_pages
                     if p.data.get('image') and str(p.data.get('image')).startswith('/images/')]
        asset_outputs.update(generate_card_thumbnails(source, out, hero_jobs, cache_dir))
    css = out / 'assets/css/site.css'
    atomic_write(css, (HERE / 'site.css').read_text(encoding='utf-8') + '\n' +
                 (HERE / 'pygments.css').read_text(encoding='utf-8'))
    asset_outputs.add('assets/css/site.css')
    script = out / 'assets/js/theme.js'
    atomic_write(script, (HERE / 'theme.js').read_text(encoding='utf-8'))
    asset_outputs.add('assets/js/theme.js')
    desired_outputs = {path.relative_to(out).as_posix() for path in written} | asset_outputs
    if incremental:
        remove_stale_outputs(out, cache.get('outputs', []), desired_outputs)
    live_sources = {document.source.relative_to(source).as_posix() for document in posts + pages + link_pages}
    document_cache = {key: value for key, value in document_cache.items() if key in live_sources}
    save_cache(cache_dir, {'version': CACHE_VERSION, 'fingerprint': fingerprint,
                           'documents': document_cache, 'outputs': sorted(desired_outputs)})
    print(f'Built {len(posts)} posts ({sum(p.draft for p in posts)} draft), {len(pages)} pages, '
          f'{len(listed)} chronological index entries at {out}')
    for path in ignored:
        print(f'Ignored post file without front matter: {path.relative_to(source)}', file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=CONTENT, help='Content directory (defaults to project content/)')
    parser.add_argument('--output', type=Path, default=PROJECT / 'site', help='Generated site/ directory')
    parser.add_argument('--incremental', action='store_true',
                        help='Reuse cached rendering and update site/ in place for fast local previews')
    parser.add_argument('--no-images', action='store_true', help='Skip copying large image directory for quick checks')
    parser.add_argument('--fail-on-drafts', action='store_true',
                        help='Refuse to build if any draft: true posts would be publicly accessible')
    parser.add_argument('--site-url', help='Explicit canonical https://domain for all generated HTML, Markdown, feed and llms.txt')
    parser.add_argument('--expected-domain',
                        help='Require content/pages/CNAME to contain this deployment domain')
    args = parser.parse_args()
    if args.expected_domain:
        cname = args.source / 'pages/CNAME'
        if not cname.is_file() or cname.read_text().strip() != args.expected_domain:
            parser.error(f'content/pages/CNAME must contain {args.expected_domain!r}')
    try:
        build(args.source, args.output, not args.no_images, args.fail_on_drafts, args.site_url,
              incremental=args.incremental)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        parser.exit(1, f'Build failed: {exc}\n')


if __name__ == '__main__':
    main()
