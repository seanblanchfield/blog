#!/usr/bin/env python3
"""Local blog preview with extensionless HTML pages; opt in to container-facing bind."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


class PreviewHandler(SimpleHTTPRequestHandler):
    extensions_map = {**SimpleHTTPRequestHandler.extensions_map, '.md': 'text/markdown; charset=utf-8'}

    def guess_type(self, path):
        if not Path(path).suffix:
            return 'text/html; charset=utf-8'
        return super().guess_type(path)


class LoopbackHTTPServer(ThreadingHTTPServer):
    allow_reuse_address = True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--bind', choices=('127.0.0.1', '0.0.0.0'), default='127.0.0.1',
                        help='Use 0.0.0.0 only behind a private, restricted Docker port mapping')
    parser.add_argument('--site', type=Path, default=HERE / 'site')
    args = parser.parse_args()
    site = args.site.resolve()
    if not site.is_dir() or not (site / 'index.html').is_file():
        parser.error(f'build the site first; no index.html at {site}')
    if not site.is_relative_to(HERE):
        parser.error('preview output must remain inside the Python project')
    if args.bind == '0.0.0.0':
        print('WARNING: Preview has no authentication and may expose direct-link drafts; '
              'restrict access at the Docker host.', flush=True)
    with LoopbackHTTPServer((args.bind, args.port), partial(PreviewHandler, directory=str(site))) as server:
        print(f'Previewing {site} on {args.bind}:{server.server_port}', flush=True)
        server.serve_forever()


if __name__ == '__main__':
    main()
