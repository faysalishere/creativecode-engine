# CreativeCode Engine — first result in two minutes

CreativeCode is a **rule-based design-direction toolkit**, not an AI website builder.

## Path A: browser-only test (about two minutes)

1. Open the [interactive design study](https://faysalishere.github.io/creativecode-engine/#directions). No install or sign-in is required.
2. Switch among **Editorial identity**, **Project dossier** and **Cinematic chapters**. Focus on navigation, hierarchy and structure, not color.
3. Go to the [2-minute user test](https://faysalishere.github.io/creativecode-engine/#quick-test). Choose the direction you would explore (or **Not sure**) and say how clearly they differ.
4. Click **Copy feedback** and, if you choose, paste it into a comment on [feedback issue #1](https://github.com/faysalishere/creativecode-engine/issues/1). GitHub sign-in is only needed to submit a comment.

**A useful result** can be either a meaningful difference you noticed or a specific reason the concepts felt too similar.

## Path B: Python CLI (about two minutes when Git and Python 3.10+ are ready)

```bash
git clone https://github.com/faysalishere/creativecode-engine.git
cd creativecode-engine
python3 -m creativecode concepts --brief examples/portfolio_brief.json --out concepts.json
```

Open `concepts.json` and inspect its three `concepts`. These are curated structures, **not automatically generated original designs**.

Optional checks:

```bash
python3 -m creativecode originality --concepts concepts.json --out originality.json
python3 -m creativecode critique --brief examples/portfolio_brief.json --concepts concepts.json --out critic.json
```

Open those JSON outputs to inspect declared differences and review questions. They do not certify aesthetic quality.

### Troubleshooting

- No `python3` command? Install Python 3.10+, or use `python` on systems where that is the executable name.
- No Git? Download the repository ZIP from GitHub, extract it and open a terminal in the extracted repository directory.
- `No module named creativecode`? Run commands **from the repository root** (the folder containing `creativecode/`).
- Bug? Open a [new issue](https://github.com/faysalishere/creativecode-engine/issues/new), including your Python version, exact steps and sanitized output.

## Data and evidence

The static site does **not** send or store answers or run hidden analytics. Copying is a deliberate user action; posting the comment is separate. This trial checks clarity, not real adoption or design certification. See the [user-testing protocol](USER_TESTING.md) and [full usage guide](USAGE.md).
