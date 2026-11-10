# 03 — Professional Design Review Scorecard (v1.0)

## Evidence-first weighted scoring

Reviewers record each criterion from **0–5** (0 = absent/poor, 3 = adequate, 5 = exceptional) with a written reason and reference to a concept/wireframe/screenshot/interaction test. The calculator computes `sum(weight * rating / 5)`.

| Criterion key | Weight | Evidence to seek |
|---|---:|---|
| `originality` | 20 | Distinct composition, information model and interaction vs generic AI templates and sibling concepts |
| `strategy` | 15 | Correct user job, audience, priorities and purposeful design rationale |
| `hierarchy` | 15 | Obvious focal point, readable scanning order, meaningful content density |
| `typography` | 10 | Consistent type scale, copy, readable bilingual wrapping, line length |
| `composition` | 10 | Grid, alignment, rhythm, useful negative space and responsive rearrangement |
| `usability` | 10 | Navigation and actions clear, full states, predictable interactions |
| `responsive` | 10 | Mobile-first adaptation; 390/768/1440 evidence when code exists |
| `motion` | 5 | Motion serves meaning, accessible reduced motion, smoothness |
| `engineering` | 5 | Real content provenance, maintainability, page speed and no regressions |
| **Total** | **100** | |

**Important:** At concept stage, untested engineering/responsive details must be recorded as unverified; scores then represent a provisional design proposal, not a shipped-quality score.

### Thresholds (project's internal rubric, not a universal standard)

- **85–100:** Candidate for user approval *only when all hard gates pass*.
- **70–84.99:** Revise before selection.
- **Below 70:** Rework concept fundamentally.
- Additional minimum: `originality` >= 3.5/5, and `usability` >= 3/5.

## Hard-gate checklist

Hard gates are recorded as `pass`, `fail`, or `not_tested` in `examples/sample_review.json` and can override high weighted scores:

| Gate | Pass criteria |
|---|---|
| `scope_preserved` | No unapproved changes to approved roadmap, design or live systems |
| `truthful_assets` | Real logos/screenshots/figures are verified or labelled mockups |
| `accessibility_baseline` | No known severe contrast, keyboard, focus or reduced-motion failures |
| `functional_integrity` | No critical broken navigation, forms or interactions (for coded deliverables) |
| `structural_distinction` | Concepts do not differ merely by color, font, shadows or animation |
| `evidence_integrity` | Scores, test results, runtime metrics and screenshots are not invented |

A gate set to `not_tested` results in **unverified** status (not a pass). Any `fail` results in **blocked** status. Approval of a concept is always human.

## Review report template

```text
Project / version:
Reviewer and date:
Stage: concept | prototype | implemented
Evidence links/paths:
Per-dimension ratings + reasons:
Weighted score (0–100):
Hard-gate statuses:
Three strengths:
Three highest-impact weaknesses:
Is direction structurally different from alternatives? Why?
Disposition: candidate | revise | rework | blocked | unverified
Retest / approval needed:
```

## What automated tools can and cannot do

**Can:** validate a scorecard schema, aggregate ratings, enforce thresholds and required gates; browser tools can detect pixel changes and broken interactions.

**Cannot reliably do alone:** prove a design is beautiful/original, verify legal rights to images, establish subjective product-market fit, or turn a screenshot match into usability certification.
