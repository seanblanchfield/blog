#!/usr/bin/env python3
"""Check local links in every generated page and stylesheet, without networking."""
import argparse
import html.parser
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

CSS_URL = re.compile(r'url\(\s*[\'\"]?([^\)\'\"]+)[\'\"]?\s*\)', re.IGNORECASE)
HTML_SUFFIXES = {'.html', '.htm'}


class References(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.urls = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('href', 'src', 'poster'):
            if attrs.get(key):
                self.urls.append((f'{tag}:{key}', attrs[key]))
        for key in ('srcset', 'imagesrcset'):
            if attrs.get(key):
                for item in attrs[key].split(','):
                    candidate = item.strip().split()[0] if item.strip() else ''
                    if candidate:
                        self.urls.append((f'{tag}:{key}', candidate))
        if attrs.get('style'):
            self.urls += [('style:url', url) for url in CSS_URL.findall(attrs['style'])]


def scan(out, host='seanblanchfield.com'):
    """Return broken local references as (source path, kind, URL, target path)."""
    out = out.resolve()
    if not (out / 'index.html').is_file():
        raise ValueError(f'No generated index at {out}')
    broken, counts = [], Counter()
    for source in out.rglob('*'):
        if not source.is_file():
            continue
        relative = source.relative_to(out)
        if source.suffix == '.css':
            refs = [('css:url', url.strip()) for url in CSS_URL.findall(source.read_text(encoding='utf-8'))]
        elif source.suffix in HTML_SUFFIXES or (not source.suffix and source.read_bytes()[:32].lower().lstrip().startswith(b'<!doctype html')):
            parser = References()
            parser.feed(source.read_text(encoding='utf-8'))
            refs = parser.urls
        else:
            continue
        served_path = '/' + relative.as_posix()
        if relative.name == 'index.html':
            served_path = '/' + relative.parent.as_posix().strip('.')
            if not served_path.endswith('/'):
                served_path += '/'
        for kind, url in refs:
            url = url.strip()
            if not url or url.startswith('#'):
                counts['fragment'] += 1
                continue
            parsed = urlsplit(urljoin(f'https://{host}{served_path}', url))
            if parsed.scheme not in {'http', 'https'} or parsed.hostname != host:
                counts['external'] += 1
                continue
            path = unquote(parsed.path).lstrip('/')
            if '\\' in path or any(part in {'.', '..'} for part in path.split('/')):
                broken.append((relative.as_posix(), kind, url, path))
                continue
            target = out / path
            html_target = target.with_name(target.name + '.html') if target.name else target
            if (target.is_file() or html_target.is_file() or
                    (target.is_dir() and (target / 'index.html').is_file())):
                counts['local'] += 1
            else:
                broken.append((relative.as_posix(), kind, url, path))
    return broken, counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, default=Path(__file__).resolve().parent.parent / 'site')
    parser.add_argument('--allow-known-source-errors', action='store_true',
                        help='Report but tolerate the four malformed links inherited from source Markdown')
    args = parser.parse_args()
    broken, counts = scan(args.site)
    for source, kind, url, target in broken:
        print(f'{source}: {kind} {url!r} -> missing /{target}')
    print(f'Checked {counts["local"]} resolving local, {counts["external"]} external, '
          f'{counts["fragment"]} fragment/empty refs; {len(broken)} broken local refs.')
    known = {
        ('2012/11/sunday-independent-18-november-2012', 'www.independent.ie'),
        ('2014/07/easy-startup-dashboards', 'vizec@tcd.ie'),
        ('2014/09/reforming-rd-tax-credits',
         'startupireland.ie/wp-content/uploads/2014/09/StartupIreland-Pre-Budget-Submission-2014-Google-Docs.pdf'),
        ('2024/05/my-smart-home-dashboard', '(https://www.twilightrender.com/)'),
    }
    actual = {(source[:-5] if source.endswith('.html') else source, url)
              for source, _, url, _ in broken}
    if broken and not (args.allow_known_source_errors and
                       actual == known and
                       all(kind == 'a:href' for _, kind, _, _ in broken) and len(broken) == 4):
        parser.exit(1, 'Unexpected broken local references.\n')
    if broken:
        print('Only the four known malformed source Markdown links remain.')


if __name__ == '__main__':
    main()
