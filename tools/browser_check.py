"""Optional local Playwright browser QA for the static portfolio preview.

Not a dependency of the core CLI or GitHub unit-test workflow.
Install Playwright and Chromium separately to run this local-only browser check.
"""
from __future__ import annotations
import sys
import shutil
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent


def run() -> int:
    out = ROOT / "artifacts" / "portfolio-browser"
    out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        binary = shutil.which("chromium") or shutil.which("google-chrome")
        launch_options = {"headless": True}
        if binary:
            launch_options["executable_path"] = binary
        browser = p.chromium.launch(**launch_options)
        try:
            for width, height in ((390,844),(768,900),(1440,900)):
                page=browser.new_page(viewport={"width":width,"height":height},device_scale_factor=1)
                errors=[]
                page.on("pageerror",lambda error:errors.append(str(error)))
                page.set_content((ROOT / "examples/portfolio_preview/index.html").read_text(encoding="utf-8"), wait_until="load")
                assert page.locator('html').get_attribute('lang')=='en'
                for cid in ('a','b','c'):
                    page.locator(f'#tab-{cid}').click()
                    assert page.locator(f'#concept-{cid}').is_visible()
                    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'), f'overflow {width} {cid}'
                    assert page.locator(f'#tab-{cid}').get_attribute('aria-selected')=='true'
                    if width in (390,1440):
                        page.screenshot(path=str(out/f'{cid}-{width}-en.png'),full_page=True)
                page.locator('#tab-b').click()
                page.locator('[data-project="3"]').click()
                assert page.locator('#dossier-title').inner_text()=='DN Connect'
                page.locator('#language').click()
                assert page.locator('html').get_attribute('lang')=='bn'
                assert 'নির্মাণাধীন' in page.locator('#dossier-role').inner_text()
                assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'), f'bn overflow {width}'
                assert not errors, f'JS errors at {width}: {errors}'
                page.close()
        finally:
            browser.close()
    print('PASS: responsive widths 390/768/1440, A/B/C, EN/BN, project interactions, no overflow/errors.')
    return 0


if __name__=='__main__':
    try: raise SystemExit(run())
    except Exception as e:
        print(f'FAIL: {e}',file=sys.stderr)
        raise
