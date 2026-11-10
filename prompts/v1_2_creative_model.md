# V1.2 — Creative model prompt (external AI assistant)

This file upgrades the existing Creative Director workflow. The local Python generator is a deterministic pattern library; it does not produce novel AI design concepts on its own. Use an AI model to critically extend or replace these starting points.

Inputs: `01_DESIGN_RULEBOOK.md`, `02_CREATIVE_WORKFLOW.md`, `examples/portfolio_brief.json` (or your own brief), `examples/portfolio_concepts.json`, and `examples/portfolio_originality.json`.

Your task:

1. Read approved brand/roadmap constraints first. Do not reinterpret this concept exploration as permission to edit or deploy any live site.
2. Independently question the three curated concept directions. Suggest genuinely new structural decisions when they suit the actual audience. Do not just rename them.
3. For each of A/B/C supply a text wireframe, desktop/mobile content order, one primary user flow, concrete use of authentic project assets, and a rationale for why this pattern is appropriate.
4. Cross-compare A/B, A/C and B/C in the five structural fields: hero composition, information architecture, navigation, content presentation, interaction. A pair must vary in at least three dimensions; font/color changes do not count.
5. Check against generic patterns: decorative emoji, generic gradient/glass cards, useless animation, fictional social proof and unnecessary giant mobile blocks. Avoid those unless a functional rationale and project approval exist.
6. Distinguish verified input, reasonable design proposals and unknown facts. Label hypothetical diagrams as conceptual, not real production screenshots.
7. Produce structured concept JSON using the same keys as `examples/portfolio_concepts.json` so the local originality tool can compare declared signatures. The JSON structure values must honestly describe the actual wireframes.
8. Return a human-readable comparison and recommend one direction, but stop before implementation until the user selects it.

Never claim the local checker can establish visual uniqueness or that AI-generated scores prove aesthetic quality. Human judgment remains the release gate.
