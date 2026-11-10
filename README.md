# CreativeCode Engine

**A practical creative direction and design-review toolkit for AI-assisted coding.**

[![CI](https://github.com/faysalishere/creativecode-engine/actions/workflows/tests.yml/badge.svg)](https://github.com/faysalishere/creativecode-engine/actions/workflows/tests.yml)
![Version](https://img.shields.io/badge/version-0.1.0-informational)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**Release: `v0.1.0` — Foundation toolkit.** No API key, server, or paid tool is required to run the included score calculator. The design workflow works with an AI assistant that can read documents and prompts; the quality of its output still requires human judgment.

> **What this is:** design rules, three AI role prompts, a repeatable concept-to-review workflow, and a Python review-score validator.  
> **What it isn't:** a trained AI model, a VS Code extension, a CLI that generates websites, an autonomous agent, or a hosted website builder.

## Why CreativeCode?

AI can produce functioning code while recycling predictable layouts: oversized hero cards, arbitrary emoji, irrelevant gradients and cosmetic-only variants. CreativeCode requires deliberate design decisions, three meaningfully different concepts and an evidence-backed critique *before* implementation. It preserves existing project decisions, and it never treats a subjective score as proof of design quality.

## Quick start (5–10 minutes)

**1. Get the project.** On GitHub, choose **Code → Download ZIP**, or clone it:

```sh
git clone https://github.com/faysalishere/creativecode-engine.git
cd creativecode-engine
```

**2. Give your AI assistant these files** (paste their text or attach them):

- `01_DESIGN_RULEBOOK.md`
- `02_CREATIVE_WORKFLOW.md`
- `prompts/creative_director.md`
- `examples/sample_brief.md` (replace with your own brief when ready)

Ask: *"Follow the creative director prompt and the rulebook. Give me three structurally different concepts, not code. Explain the differences and unresolved assumptions."*

**3. Review the concepts.** Supply `03_REVIEW_SCORECARD.md` and `prompts/design_critic.md` in a separate review. Do **not** mark visual, functional or accessibility tests as passed unless you have evidence. Choose a concept yourself; don't let an AI score make the final approval.

**4. Run the score calculator** (optional; requires Python 3.10+ and no external packages):

```sh
python3 tools/score.py examples/sample_review.json
python3 -m unittest discover -s tools -p 'test_*.py' -v
```

The included review is **fictional example data**. Its `UNVERIFIED` result is expected because no actual app was tested.

**5. Implement only after approval.** For a real codebase, read `prompts/implementation_engineer.md` and ask the assistant to inspect existing source before editing. Build and test in an isolated development environment; never assume a prompt authorizes deployment.

See [the detailed usage guide](docs/USAGE.md) and [বাংলায় শুরু করার নির্দেশনা](docs/GETTING_STARTED.bn.md).

## What's included?

| Path | What it does |
| --- | --- |
| `01_DESIGN_RULEBOOK.md` | Visual hierarchy, anti-generic rules, responsiveness, accessibility, motion and architecture |
| `02_CREATIVE_WORKFLOW.md` | Scope → research → distinct concepts → critique → approval → prototype → QA |
| `03_REVIEW_SCORECARD.md` | Nine weighted criteria, hard gates, evidence rules |
| `prompts/creative_director.md` | Create three substantive design concepts |
| `prompts/design_critic.md` | Challenge generic or unsupported design decisions |
| `prompts/implementation_engineer.md` | Implement one approved concept with minimal changes |
| `tools/score.py` | Local standard-library score calculation and hard-gate validation |
| `tools/test_score.py` | Unit tests of valid/invalid ratings and release gates |
| `examples/sample_brief.md` | Fictional, privacy-safe example brief |
| `examples/three_concepts.md` | Example of three structurally different approaches |
| `examples/sample_review.json` | Fictional scorecard input; **not** real QA evidence |
| `docs/` | Practical usage, Bangla instructions and attribution |

## Scoring principles

The score is a weighted sum of human/AI-supplied ratings from 0–5, normalized to 100. Passing all the hard gates is required even to become a *candidate for human approval*. A `fail` returns `BLOCKED`; `not_tested` returns `UNVERIFIED`. The tool does **not** inspect screenshots, verify licenses, execute Playwright, or generate code. Read [the full rubric](03_REVIEW_SCORECARD.md).

## Compatibility and privacy

- Files are plain Markdown and JSON; use them with any model that can receive file content.
- The Python script uses only the standard library and does not call an API or upload data.
- A separate AI provider may have its own subscription, usage limits or data-handling policy.
- Keep private client briefs, personal data and production secrets out of public issues and repository files. Provide AI services only the information you are permitted to share.
- This package does not create a persistent design memory, autonomously browse or run browser QA. Those are future possibilities, not included features.

## Project status

- **v0.1.0:** published-source-ready manual workflow, prompts, examples and validated scoring script.
- **Future (not included):** local concept prototypes, screenshot-based QA integrations, installable agent, web platform.

## Contributing and security

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for scope and checks and [SECURITY.md](SECURITY.md) for reporting concerns. Please open an issue describing the problem before proposing architectural rewrites.

## License and credits

MIT licensed. See [LICENSE](LICENSE) and [docs/ATTRIBUTION.md](docs/ATTRIBUTION.md). Upstream design references are acknowledged but are **not** distributed as part of this repository.
