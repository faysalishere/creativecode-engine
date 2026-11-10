# 02 — Creative Concept Generation Workflow (v1.0)

## Role sequence

The same model can operate in stages; initially no costly multi-agent infrastructure is needed. Separate creation from criticism, preferably with a clean review pass.

### Stage 0 — Scope lock

Inputs: current approved roadmap, intended project, existing code/visuals, target users, known constraints, available assets and allowed environment.

Output: a `PROJECT BRIEF` with **in scope**, **out of scope**, **evidence available**, **missing facts** and **approval boundary**. Do not change code.

### Stage 1 — Design research

Review actual user tasks, 3–5 category references where available, then extract principles (not clone pixel arrangement). Identify common AI-looking tropes in the niche, UX risk points, and meaningful differentiators. Link to verified references or mark unverified.

### Stage 2 — Generate three concept directions

Every concept must differ in **at least three structural dimensions**: information architecture, composition, navigation, content presentation, interaction model. This comparison is required before any code.

Deliver each with:
- Concept name + 1-sentence strategic thesis.
- Named audience / primary user task.
- Text-based wireframe from top to bottom for mobile + desktop.
- Layout features, typography roles, authentic asset plan.
- Key actions and behavior, motion only where useful.
- Differences versus the other two directions.
- Feasibility/complexity and accessibility risks.

### Stage 3 — Adversarial review

A separate review pass challenges weak assumptions. Score each concept against `03_REVIEW_SCORECARD.md` and explain evidence. The reviewer must flag cosmetic-only variation, inaccessible patterns, false content, roadmap conflicts and implementation overhead. **Do not assign real scores without real evidence.**

Gate: no blocked constraints, real differences, user choice of direction before implementation.

### Stage 4 — Prototyping (future / approval-gated)

Build one approved direction in a separate local/staging folder. Reuse verified assets, implement design tokens and component architecture. No existing production file modifications. Build vertical slices, not a rewrite of the whole site per iteration.

### Stage 5 — Visual and functional QA (future)

Capture comparable screenshot baselines under same OS/browser/viewport/fonts. At minimum 390px, ~768px, 1440px; both languages where applicable. Test keyboard and touch behavior, navigation, forms, mobile overflow, reduced motion and real content. Use automated screenshot diffs to locate regressions; human reviewer must assess aesthetics and usability.

### Stage 6 — Fix and re-score (future)

For each issue record `symptom → root cause → minimal fix → retest → evidence`. Maximize impact per change; do not polish low-impact details while core information hierarchy remains weak. Re-score; no self-declared pass without recorded evidence.

### Stage 7 — Release review (future / approval-gated)

Present code diff, tests, known limitations, performance readings and rollback plan. Production deployment requires user approval. A passing screenshot test is not authorization to deploy.

## Feedback memory (without training a new model)

For each reviewed design, capture a small record:

```yaml
project: sample-project
concept_id: C01
reviewer: human-or-model
accepted: false
reason: "Project hierarchy remains a generic card grid"
keep: ["Editorial title hierarchy", "Meaningful real asset focus"]
change: ["Different project presentation", "Tighter mobile sections"]
evidence: ["reviewer notes", "screenshot paths when available"]
```

Collecting these records is not the same as model fine-tuning. It provides grounded examples for later prompting and comparison.

## Iteration contract

- Preserve previous approved decisions by default.
- If a design direction must change, propose the change and ask permission before altering the selected implementation.
- Track complete / current / next; never quietly abandon a rejected or unresolved issue.
- Separate conceptual quality claims from implementation and live QA results.
