import tempfile
import unittest
from pathlib import Path

from build import (CONTENT, PROJECT, build, load_frontmatter, meta_description,
                   normalize_lists, output_path, post_url, render_markdown, split_excerpt)
from check_artifact import validate


class BlogTests(unittest.TestCase):
    def test_source_permalinks(self):
        path = CONTENT / 'posts/2025-03-26-ai-org-conversation-framework.md'
        metadata, _ = load_frontmatter(path)
        self.assertEqual(post_url(metadata, metadata['date'], path.name), '/2025/03/ai-org-conversation-framework')

    def test_markdown_compatibility(self):
        text = render_markdown('Meeting Time\n\nPlease consider:\n- Is someone chairing?\n- Clear goal?\n\nUse ~~Twitter~~ *X*.')
        self.assertIn('<ul>', text)
        self.assertIn('<li>Is someone chairing?</li>', text)
        self.assertIn('<del>Twitter</del>', text)
        self.assertEqual(normalize_lists('````\n- literal\n````\n'), '````\n- literal\n````\n')

    def test_metadata_text_is_clean_and_excerpt_markers_are_compatible(self):
        self.assertEqual(split_excerpt('Before<!--more-->After'), 'Before')
        self.assertEqual(split_excerpt('Before<!-- more -->After'), 'Before')
        result = meta_description('', '<p>A &amp; B with enough words to test clean truncation.</p>', limit=22)
        self.assertLessEqual(len(result), 23)  # ellipsis may occupy the final character
        self.assertNotIn('&amp;', result)
        self.assertFalse(result[:-1].endswith(' '))

    def test_pygments_highlights_known_languages_without_guessing(self):
        for language, snippet in [('python', 'print("hi")'), ('yaml', 'name: example'),
                                  ('bash', 'echo hello'), ('actionscript', 'var n:int = 1;')]:
            with self.subTest(language=language):
                rendered = render_markdown(f'```{language}\n{snippet}\n```')
                self.assertIn('class="codehilite"', rendered)
                self.assertIn('<span class=', rendered)
                self.assertIn('<pre>', rendered)
        for language in ('', 'not-a-real-lexer'):
            with self.subTest(language=language):
                rendered = render_markdown(f'```{language}\njust a sentence\n```')
                self.assertIn('just a sentence', rendered)
                self.assertNotIn('class="k"', rendered)
                self.assertNotIn('class="s"', rendered)
        self.assertIn('Canonical:', render_markdown('Canonical: example'))

    def test_post_fences_are_labelled(self):
        import re
        for source in (CONTENT / 'posts').glob('*.md'):
            lines = source.read_text(encoding='utf-8-sig').splitlines()
            opened = None
            for number, line in enumerate(lines, start=1):
                fence = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
                if not fence:
                    continue
                marker, suffix = fence.groups()
                if opened is None:
                    self.assertRegex(suffix, r'^\s*[\w+-]+\s*$', f'{source}:{number} needs a language label')
                    opened = (marker[0], len(marker))
                elif marker[0] == opened[0] and len(marker) >= opened[1] and not suffix.strip():
                    opened = None
            self.assertIsNone(opened, f'{source} has an unclosed fence')

    def test_public_build_excludes_drafts_completely(self):
        site = PROJECT / 'site'
        cache = PROJECT / '.build-cache-test-drafts'
        try:
            build(CONTENT, site, copy_images=False, exclude_drafts=True,
                  incremental=True, cache_dir=cache)
            slug = '2026/10/dublin-declaration-ai'
            self.assertFalse((site / f'{slug}.html').exists())
            self.assertFalse((site / f'{slug}.md').exists())
            for path in ('index.html', 'feed.xml', 'sitemap.xml', 'llms.txt'):
                self.assertNotIn('dublin-declaration-ai', (site / path).read_text())
        finally:
            import shutil
            shutil.rmtree(cache, ignore_errors=True)

    def test_incremental_build_reuses_cache_and_removes_owned_stale_output(self):
        import hashlib
        site = PROJECT / 'site'
        cache = PROJECT / '.build-cache-test'
        try:
            # A no-images test must not clean the shared preview output: doing so removes every
            # image from site/ and leaves the running preview full of broken image links.
            preserved_image = site / 'images/default_featured_image.jpg'
            self.assertTrue(preserved_image.is_file(), 'run a full build before the test suite')
            build(CONTENT, site, copy_images=False, exclude_drafts=True,
                  incremental=True, cache_dir=cache)
            self.assertTrue(preserved_image.is_file())
            baseline = hashlib.sha256((site / 'about/index.html').read_bytes()).hexdigest()
            stale = site / 'obsolete-generated-file.html'
            stale.write_text('old')
            import json
            manifest = json.loads((cache / 'manifest.json').read_text())
            manifest['outputs'].append('obsolete-generated-file.html')
            (cache / 'manifest.json').write_text(json.dumps(manifest))
            build(CONTENT, site, copy_images=False, exclude_drafts=True,
                  incremental=True, cache_dir=cache)
            self.assertEqual(hashlib.sha256((site / 'about/index.html').read_bytes()).hexdigest(), baseline)
            self.assertFalse(stale.exists())
            self.assertTrue((cache / 'manifest.json').is_file())
        finally:
            import shutil
            shutil.rmtree(cache, ignore_errors=True)

    def test_output_guard(self):
        with tempfile.TemporaryDirectory(dir=PROJECT) as temp:
            root = Path(temp)
            self.assertEqual(output_path(root, '/2026/08/name'), root / '2026/08/name.html')
            with self.assertRaises(ValueError):
                output_path(root, '/../../outside')
            with self.assertRaisesRegex(ValueError, 'site/'):
                build(CONTENT, root / 'site', copy_images=False)
            with self.assertRaisesRegex(ValueError, 'pages/_config.yml'):
                build(root, PROJECT / 'site', copy_images=False)

    def test_artifact(self):
        site = PROJECT / 'site'
        if not (site / 'index.html').exists():
            self.skipTest('Build the site before running artifact checks')
        self.assertEqual(validate(CONTENT, site, forbid_drafts=True), [])
        with self.subTest('delisted posts stay reachable but unlisted'):
            self.assertTrue((site / '2008/06/im-a-complainer.html').is_file())
            delisted = (site / 'llms.txt').read_text().split('## Delisted', 1)[1]
            self.assertIn('/2008/06/im-a-complainer.md', delisted)
            self.assertIn('/2008/09/collision-free.md', delisted)
            index_heading = (site / 'index.html').read_text()
            self.assertNotIn('/2008/09/o2-ireland-overcharging-me-for-data-roaming/', index_heading)
            self.assertNotIn('/2011/05/natty-narwhal-had-my-laptop-for-lunch/', index_heading)
            self.assertNotIn('Boxee Box', index_heading)
            self.assertNotIn('/boxee-box-fail/', (site / 'llms.txt').read_text().split('## Delisted')[0])
        self.assertTrue((site / 'page/3/index.html').is_file())
        self.assertFalse((site / 'page/4/index.html').is_file())
        self.assertFalse((site / 'archive/index.html').exists())
        self.assertFalse((site / 'archive/page/2/index.html').exists())
        self.assertTrue((site / '2011/07/the-dangers-of-excessive-effectiveness.md').is_file())
        self.assertIn('href="/how-i-work"', (site / 'about/index.html').read_text())
        self.assertTrue((site / 'ai-ireland-podcast.md').is_file())
        working = (site / 'how-i-work/index.html').read_text()
        self.assertIn('<del>Twitter</del>', working)
        self.assertRegex(working, r'(?s)Meeting Time</h1>.*?<ul>.*?<li>Is someone chairing', 'Meeting Time list')
        moved = (site / 'working-with-me/index.html').read_text()
        self.assertIn('http-equiv="refresh" content="0;url=/how-i-work/"', moved)
        self.assertTrue((site / 'working-with-me.md').is_file())
        index = (site / 'index.html').read_text()
        self.assertIn('<a href="/about/">Bio</a>', index)
        self.assertNotIn('href="/how-i-work/"', index)  # hidden page, linked only from Bio
        self.assertIn('<h1>Bio</h1>', (site / 'about/index.html').read_text())
        self.assertIn('<h1>How I work</h1>', working)
        self.assertNotIn('href="/archive/"', index)
        self.assertIn('href="/page/2/"', index)
        llm_cta = (CONTENT / 'pages/llm-cta.md').read_text().strip()
        llms_text = (site / 'llms.txt').read_text()
        self.assertTrue(llms_text.startswith(llm_cta + '\n\n---\n'))
        self.assertIn('/2026/10/the-giants-dont-die.md', llms_text)
        article_md = (site / '2026/10/the-giants-dont-die.md').read_text()
        self.assertTrue(article_md.startswith(llm_cta + '\n\n---\n'))
        self.assertIn('follow Sean Blanchfield on LinkedIn', article_md)
        self.assertIn('RSS feed', article_md)
        self.assertIn('Dark mode', index)
        self.assertIn('class="skip-link" href="#main-content"', index)
        self.assertIn('<main id="main-content"', index)
        self.assertIn('application/ld+json', index)
        article = (site / '2026/10/the-giants-dont-die.html').read_text()
        self.assertIn('"@type":"BlogPosting"', article)
        self.assertIn('itemprop="author"', article)
        self.assertIn('article:published_time', article)
        self.assertIn('twitter:card', article)
        sitemap = (site / 'sitemap.xml').read_text()
        self.assertIn('https://seanblanchfield.com/2026/10/the-giants-dont-die', sitemap)
        self.assertNotIn('.md</loc>', sitemap)
        self.assertNotIn('/404.html</loc>', sitemap)
        self.assertIn('Sitemap: https://seanblanchfield.com/sitemap.xml',
                      (site / 'robots.txt').read_text())
        feed = (site / 'feed.xml').read_text()
        self.assertIn('<author><name>Sean Blanchfield</name>', feed)
        self.assertIn('<published>', feed)
        self.assertIn('type="text/markdown"', feed)
        self.assertIn('.codehilite .k', (site / 'assets/css/site.css').read_text())
        technical = (site / '2024/07/restore-corrupted-ha-database.html').read_text()
        self.assertIn('class="codehilite"', technical)
        self.assertIn('<span class=', technical)
        portable = (site / '2024/07/restore-corrupted-ha-database.md').read_text()
        self.assertIn('```bash', portable)
        self.assertNotIn('<span class=', portable)

    def test_symlink_output_guard(self):
        with tempfile.TemporaryDirectory(dir=PROJECT) as temp:
            real = Path(temp) / 'real'
            real.mkdir()
            alias = Path(temp) / 'alias'
            alias.symlink_to(real, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, 'symlinked'):
                build(CONTENT, alias, copy_images=False)


if __name__ == '__main__':
    unittest.main()
