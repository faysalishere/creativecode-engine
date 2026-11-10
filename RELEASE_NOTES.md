# CreativeCode Engine v0.2.0 — Design Intelligence

A free offline toolkit for exploring **three distinct design structures** before writing AI-assisted code.

## Included
- Python 3.10+ CLI with curated architectures for portfolio, directory and product briefs.
- Pairwise declared-structure originality heuristic; not pixel-level analysis.
- Evidence-gated independent critic packet; no fabricated visual scores.
- Local concept-only bilingual portfolio preview (A Editorial / B Dossier / C Chapters).
- Existing prompt workflow, design rulebook, score calculator and tests.

## Quick start
```bash
git clone https://github.com/faysalishere/creativecode-engine.git
cd creativecode-engine
python3 -m creativecode concepts --brief examples/portfolio_brief.json --out concepts.json
python3 -m creativecode originality --concepts concepts.json --out originality.json
python3 -m creativecode critique --brief examples/portfolio_brief.json --concepts concepts.json --out critic.json
```

No API key or package installation required for the CLI. AI model integration, automatic site generation, visual originality certification and hosted deployment are **not included**.

Read the [README](https://github.com/faysalishere/creativecode-engine#readme) and [বাংলা নির্দেশনা](https://github.com/faysalishere/creativecode-engine/blob/main/docs/GETTING_STARTED.bn.md).
