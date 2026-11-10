"""Deployment-safe static-site checks for the CreativeCode GitHub Pages demo."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import unittest

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / 'docs'


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.refs = []
        self.controls = []
        self.title = ''
        self.has_main = False
        self.has_h1 = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if 'href' in attrs:
            self.refs.append(attrs['href'])
        if 'src' in attrs:
            self.refs.append(attrs['src'])
        if 'aria-controls' in attrs:
            self.controls.append(attrs['aria-controls'])
        if tag == 'main':
            self.has_main = True
        if tag == 'h1':
            self.has_h1 = True


class DemoSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (DOCS / 'index.html').read_text(encoding='utf-8')
        cls.parser = References()
        cls.parser.feed(cls.html)

    def test_exists_and_has_nojekyll(self):
        self.assertTrue((DOCS / '.nojekyll').is_file())
        self.assertTrue((DOCS / 'assets/site.css').is_file())
        self.assertTrue((DOCS / 'assets/site.js').is_file())

    def test_page_structure(self):
        self.assertTrue(self.parser.has_main)
        self.assertTrue(self.parser.has_h1)
        self.assertEqual(len(self.parser.ids), len(set(self.parser.ids)), 'Duplicate element id')
        self.assertIn('viewport', self.html)
        self.assertIn('description', self.html)

    def test_all_local_links_and_assets_exist(self):
        ids = set(self.parser.ids)
        for ref in self.parser.refs:
            parsed = urlparse(ref)
            if parsed.scheme in ('https', 'mailto', 'tel') or ref.startswith('//'):
                continue
            if ref.startswith('#'):
                self.assertIn(unquote(ref[1:]), ids, ref)
                continue
            self.assertFalse(parsed.scheme, f'Unexpected protocol in {ref}')
            self.assertTrue((DOCS / unquote(parsed.path)).exists(), f'Missing page asset: {ref}')

    def test_controls_and_tabs_resolve(self):
        ids = set(self.parser.ids)
        for target in self.parser.controls:
            self.assertIn(target, ids)
        for concept in ('editorial', 'dossier', 'chapters'):
            self.assertIn(f'id="tab-{concept}"', self.html)
            self.assertIn(f'id="panel-{concept}"', self.html)

    def test_og_image_and_pilot_are_real(self):
        self.assertTrue((DOCS / 'assets/social-preview.png').is_file())
        self.assertEqual((DOCS / 'demo/portfolio/index.html').read_bytes(),
                         (ROOT / 'examples/portfolio_preview/index.html').read_bytes())


if __name__ == '__main__':
    unittest.main()
