# CreativeCode Engine — GitHub Pages deployment

This repository includes an independent static website under `docs/`. It is intentionally separate from the Python engine and the existing portfolio prototype. The site requires no external JavaScript framework, tracking, API key, paid hosting, or backend.

## One-time activation (repository owner)

1. Open [repository Settings → Pages](https://github.com/faysalishere/creativecode-engine/settings/pages).
2. Under **Build and deployment → Source**, select **Deploy from a branch**.
3. For **Branch**, select `main`; for the folder, select `/docs`.
4. Click **Save**. GitHub automatically publishes this folder, including `docs/index.html`.
5. Open **https://faysalishere.github.io/creativecode-engine/** and use the concept switcher and **Open full interactive pilot** link to check the site. It can take a short period for the Pages build to complete.

GitHub Pages has to be activated by someone with appropriate repository permissions. The connected GitHub content-editing integration may not support changing repository Pages settings. Until this step is performed and the public URL is checked, the demo is **committed but not verified live**.

## Source layout

- `docs/index.html` — editorial product landing and interactive structure gallery
- `docs/assets/site.css`, `docs/assets/site.js` — static styling and local interaction; no third-party scripts
- `docs/assets/brand.svg`, `docs/assets/social-preview.png` — branded assets
- `docs/demo/portfolio/index.html` — unmodified copy of the earlier interactive portfolio concept prototype
- `docs/.nojekyll` — prevents Jekyll from changing or excluding asset paths

## Safety and maintenance

- Do not publish secrets, user data or confidential client briefs in the Pages directory; Pages is public.
- The original `examples/portfolio_preview/index.html` and the entire `creativecode/` Python package remain untouched.
- On future `main` commits modifying the `docs/` directory, GitHub Pages rebuilds automatically.
- `python3 -m unittest discover -s tools -p 'test_*.py' -v` validates link paths, structure and pilot integrity alongside existing engine tests.
- For advanced browser QA, run a Playwright test against the live URL; passing structural tests alone is not equivalent to live deployment verification.

## Verify publication

Check the GitHub Actions Pages run is successful, then confirm `200 OK` for both:

- `https://faysalishere.github.io/creativecode-engine/`
- `https://faysalishere.github.io/creativecode-engine/demo/portfolio/`

If `404` appears, first check Settings → Pages for the selected source and any build errors. Never claim the site is live without checking its public URL.
