# Portfolio pilot review — 2026-11-10

**Project:** MD Faysal Ahmed cinematic portfolio · concept exploration only.

**Approved design constraints respected:** near-black/crimson editorial identity, English default and Bangla toggle, exact featured-project order, truthful labels (DN Connect is in development), no real screenshot or portrait substituted, no contact address exposed, no live deployment.

## Structural comparison

The offline tool reports **PASS** for all three concept pairs. Every pair has five distinct declared structure fields, exceeding the minimum three. This proves only that the named architecture records differ; it cannot prove actual originality or taste.

| Criterion | A: Editorial flagship | B: Project dossier | C: Cinematic chapters |
|---|---|---|---|
| First visual priority | Identity + portrait frame | Project record | Manifesto |
| Information architecture | Identity → stories | Dossiers first | Thematic chapters |
| Navigation | Section anchors | Project index | Chapter navigation |
| Content presentation | Full-width editorial work | Selectable project dossier | Numbered chapter index |
| Distinct interaction | Scroll to work | Select a project | Skip to chapter |
| Practical advantage | Cohesive identity | Fast work scanning | Strong narrative rhythm |
| Principal risk | Long page | Hidden detail / focus requirements | Over-designed navigation / performance |

**Review recommendation for discussion, not approval:** A is closest to the currently approved cinematic editorial direction. B offers a work-first structure for users scanning the portfolio. C is the riskiest direction to implement without losing direct access to real work. These are hypotheses, not usability findings.

## Local technical testing

- Python: 37 unit tests pass (16 V1 regression tests plus 21 V1.2 tests).
- Generated `examples/portfolio_concepts.json`, `examples/portfolio_originality.json`, and `examples/portfolio_critic_packet.json` reproducibly.
- Chromium / Playwright local static preview: widths **390 / 768 / 1440 px**, all A/B/C tabs visible and navigable, no page-level JS errors, no horizontal overflow detected in tested states, Dossier selection works, language toggle to BN works. Screenshots captured locally for A/B/C at 390 and 1440 px.
- The screenshot inspection represents a single browser engine and pilot fixture. Browser results do not prove WCAG AA compliance, cross-device parity, good aesthetics, accessibility of every possible state, 60 FPS performance or real customer preference.

## Explicit exclusions

- No live site write, no VPS change, no external AI API call, no model training, no image synthesis, no public asset copying.
- No independent human rating or 0–100 overall design-quality score; `examples/portfolio_critic_packet.json` intentionally has null ratings.
- No GitHub Pages deployment, no user-facing production portfolio implementation.

## Next decision gate

Before developing one design for the real portfolio, the user must approve a direction and any deviation from the existing approved reference-video layout. The current approved portfolio cannot be silently replaced by any of these experiments.
