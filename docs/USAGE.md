# Detailed usage guide

No installation is necessary for the design workflow. The repository contains Markdown prompts you provide to your preferred AI assistant. The only executable component is the optional Python score calculator.

## Step 1: Write a scoped brief

Start from `examples/sample_brief.md`, replacing the fictional details with your own. Include audience, tasks, approved design decisions, forbidden changes, real asset availability and exactly what you want from the AI this iteration. Do not put credentials, personal data or client secrets in a public repository.

## Step 2: Generate *different* directions

Supply `01_DESIGN_RULEBOOK.md`, `02_CREATIVE_WORKFLOW.md`, `prompts/creative_director.md` and your brief to your AI assistant.

Ask the assistant to generate three concepts in a **single response**, with unique hierarchy, content model, navigation, and mobile/desktop composition. Cross-check structural dimensions using `examples/three_concepts.md`. Reject a color-swap as an alternative.

## Step 3: Adversarial review

For a separate review, supply the three concepts plus `03_REVIEW_SCORECARD.md` and `prompts/design_critic.md` to an AI reviewer or a human designer. Require evidence for each score and gate. Unimplemented or untested functionality is `not_tested`, not `pass`.

## Step 4: Score the review

Make a copy of `examples/sample_review.json`, fill in your observations, and run:

```sh
python3 tools/score.py my_review.json
```

Sample output shape:

```json
{
  "project": "fictional-demo-only",
  "score": 77.0,
  "status": "UNVERIFIED",
  "unverified_gates": ["accessibility_baseline", "functional_integrity"],
  "failed_gates": [],
  "note": "Recorded ratings are reviewer judgments, not automated design proof."
}
```

`UNVERIFIED` means your evidence is incomplete. Weighted ratings are subjective assessments. The calculator does **not** automatically test visuals, copy, code or original work.

## Step 5: Implementation only after selection

Once a person approves one concept and the environment, use `prompts/implementation_engineer.md`. In an existing project, audit current code first and preserve approved features. Work in a safe local or staging environment. Record actual test evidence before release. Never deploy a live system based only on a score.

## Script prerequisites

- Python 3.10 or newer.
- No pip install and no internet required.
- Run tests with `python3 -m unittest discover -s tools -p 'test_*.py' -v`.

## FAQ

**Does the tool run the AI?** No. You give the prompts to your AI assistant.

**Can I use ChatGPT, Claude or another model?** Yes, if you can provide the model with the included text. Behavior varies by provider and model.

**Does it generate websites automatically?** No. Coding is delegated to your chosen AI after a human approves a concept.

**Can scores certify visual quality?** No. The script checks reviewer entries, not the actual design.

**Will it upload my content?** The included Python calculator runs locally without network calls. Your AI provider may have separate policies.
