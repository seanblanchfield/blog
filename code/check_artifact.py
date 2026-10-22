#!/usr/bin/env python3
"""Fail if a generated Pages artifact omits required pages or contains source files."""
import argparse
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build import load_frontmatter, output_path, parse_date, post_url

POST_NAME = re.compile(r'^\d{4}-\d{2}-\d{2}-.+\.md$')
REQUIRED = ('index.html', 'about/index.html', 'page/2/index.html',
            '404.html', 'feed.xml', 'sitemap.xml', 'robots.txt', 'llms.txt',
            'assets/css/site.css')
FORBIDDEN_NAMES = {'.env', 'AGENTS.md', 'Gemfile', 'Gemfile.lock', '_config.yml',
                   'requirements.txt', 'build.py', 'check_links.py', 'check_artifact.py'}


def validate(source, site, require_cname=False, forbid_drafts=False, expected_domain=None,
             allow_config_url_mismatch=False):
    source, site = source.resolve(), site.resolve()
    issues = []
    for name in REQUIRED:
        if not (site / name).is_file():
            issues.append(f'Missing required output: {name}')
    for item in site.rglob('*'):
        relative = item.relative_to(site)
        if any(part.startswith('.') or part in {'_posts', '_sass', 'vendor', '.git', '.venv', 'node_modules'}
               for part in relative.parts) or item.name in FORBIDDEN_NAMES:
            issues.append(f'Forbidden source/private artifact: {relative}')
        if item.is_symlink():
            issues.append(f'Symlink in artifact: {relative}')
    for path in sorted(source.glob('posts/*.md')):
        parsed = load_frontmatter(path)
        if not parsed:
            continue
        meta, _ = parsed
        if not POST_NAME.match(path.name):
            issues.append(f'Unexpected source post filename: {path.relative_to(source)}')
            continue
        url = post_url(meta, parse_date(meta.get('date'), path.name), path.name)
        if meta.get('redirect_to'):
            html_output = output_path(site, unquote(url))
            for candidate in (html_output, output_path(site, unquote(url.rstrip('/') + '.md'))):
                if not candidate.is_file():
                    issues.append(f'Missing redirect stub output: {candidate.relative_to(site)}')
            continue
        output = output_path(site, unquote(url))
        if forbid_drafts and meta.get('draft') is True:
            issues.append(f'Draft source post not allowed in public artifact: {path.relative_to(source)}')
        for candidate in (output, output_path(site, unquote(url + '.md'))):
            if not candidate.is_file():
                issues.append(f'Missing post output: {candidate.relative_to(site)}')
    cname = source / 'pages/CNAME'
    if require_cname:
        if not cname.is_file():
            issues.append('Missing source CNAME')
        elif not (site / 'CNAME').is_file():
            issues.append('Missing artifact CNAME')
        elif (site / 'CNAME').read_bytes() != cname.read_bytes():
            issues.append('Artifact CNAME differs from source')
    if expected_domain:
        from yaml import safe_load
        if not expected_domain or expected_domain.strip() != expected_domain or '/' in expected_domain:
            issues.append(f'Invalid expected domain: {expected_domain!r}')
        source_url = safe_load((source / 'pages/_config.yml').read_text()).get('url', '')
        configured = urlsplit(str(source_url)).hostname
        if configured != expected_domain and not allow_config_url_mismatch:
            issues.append(f'Site URL domain {configured!r} differs from expected {expected_domain!r}')
        if cname.is_file() and cname.read_text().strip() != expected_domain:
            issues.append(f'Source CNAME domain differs from expected {expected_domain!r}')
        if (site / 'CNAME').is_file() and (site / 'CNAME').read_text().strip() != expected_domain:
            issues.append(f'Artifact CNAME domain differs from expected {expected_domain!r}')
    if expected_domain:
        expected_url = f'https://{expected_domain}'
        for item in site.rglob('*'):
            if not item.is_file() or item.is_symlink():
                continue
            rel = item.relative_to(site).as_posix()
            if item.suffix == '.html' or (not item.suffix and item.read_bytes()[:32].lstrip().lower().startswith(b'<!doctype html')):
                text = item.read_text(encoding='utf-8')
                canonical = re.search(r'<link rel="canonical" href="([^"]+)"', text)
                if canonical and urlsplit(canonical.group(1)).hostname != expected_domain:
                    issues.append(f'Canonical domain mismatch: {rel}')
            elif item.suffix == '.md' and re.match(r'^\d{4}/\d{2}/', rel):
                text = item.read_text(encoding='utf-8')
                canonical = re.search(r'^Canonical: (https?://\S+)$', text, re.MULTILINE)
                if canonical and urlsplit(canonical.group(1)).hostname != expected_domain:
                    issues.append(f'Markdown canonical domain mismatch: {rel}')
        feed = site / 'feed.xml'
        if feed.is_file():
            tree = ET.parse(feed)
            for item in tree.iter():
                if item.tag.rsplit('}', 1)[-1] in {'id', 'link'}:
                    url = item.get('href') if item.tag.endswith('link') else item.text
                    if url and urlsplit(url).scheme in {'http', 'https'} and urlsplit(url).hostname != expected_domain:
                        issues.append('Atom feed URL domain mismatch')
                        break
        index = site / 'llms.txt'
        if index.is_file():
            for raw in re.findall(r'\]\((https?://[^)]+)\)', index.read_text(encoding='utf-8')):
                if urlsplit(raw).hostname != expected_domain:
                    issues.append(f'llms.txt URL domain mismatch: {raw}')
    if (site / 'feed.xml').is_file():
        try:
            feed = ET.parse(site / 'feed.xml')
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            if feed.find('atom:author/atom:name', ns) is None:
                issues.append('Atom feed is missing its author')
            for entry in feed.findall('atom:entry', ns):
                if entry.find('atom:published', ns) is None:
                    issues.append('Atom entry is missing published timestamp')
                    break
        except ET.ParseError as error:
            issues.append(f'Invalid Atom feed: {error}')
    if (site / 'sitemap.xml').is_file():
        try:
            sitemap = ET.parse(site / 'sitemap.xml')
            ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            locations = [node.text or '' for node in sitemap.findall('sm:url/sm:loc', ns)]
            if not locations or any(not value.startswith('https://') for value in locations):
                issues.append('Sitemap contains no canonical HTTPS URLs')
            if any(value.endswith(('.md', '/404.html')) for value in locations):
                issues.append('Sitemap contains a Markdown or 404 URL')
        except ET.ParseError as error:
            issues.append(f'Invalid sitemap: {error}')
    if (site / 'robots.txt').is_file() and 'Sitemap: https://' not in (site / 'robots.txt').read_text():
        issues.append('robots.txt does not advertise an HTTPS sitemap')
    if (site / 'llms.txt').is_file():
        text = (site / 'llms.txt').read_text(encoding='utf-8')
        in_delisted = False
        for line in text.splitlines():
            if line.startswith('## '):
                in_delisted = line.startswith('## Delisted')
                continue
            for raw in re.findall(r'\]\((https?://[^)]+\.md)\)', line):
                path = unquote(urlsplit(raw).path.lstrip('/'))
                if not (site / path).is_file():
                    stripped = raw[:raw.rfind('.md')].rstrip('/')
                    target = output_path(site, '/' + unquote(urlsplit(stripped).path.lstrip('/')))
                    if in_delisted and target.is_file():
                        continue
                    issues.append(f'Broken llms.txt Markdown entry: {raw}')
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=Path(__file__).resolve().parent.parent / 'content')
    parser.add_argument('--site', type=Path, default=Path(__file__).resolve().parent.parent / 'site')
    parser.add_argument('--require-cname', action='store_true')
    parser.add_argument('--forbid-drafts', action='store_true')
    parser.add_argument('--expected-domain', help='Require generated URLs and source/artifact CNAME to match')
    parser.add_argument('--allow-config-url-mismatch', action='store_true',
                        help='Permit source _config.yml URL mismatch only when the generator uses --site-url')
    args = parser.parse_args()
    issues = validate(args.source, args.site, args.require_cname, args.forbid_drafts,
                      args.expected_domain, args.allow_config_url_mismatch)
    if issues:
        parser.exit(1, '\n'.join(issues) + '\n')
    print('Artifact check passed: expected post files, pages, Markdown entries, and clean static output.')


if __name__ == '__main__':
    main()
