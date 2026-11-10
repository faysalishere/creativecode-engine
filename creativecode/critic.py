"""Build an evidence-based critical review packet without inventing design scores."""

from __future__ import annotations
from typing import Any
from .concepts import validate_brief
from .originality import compare

REVIEW_FIELDS = (
    "originality", "strategy", "hierarchy", "typography", "composition",
    "usability", "responsive", "motion", "engineering",
)


def prepare(brief: Any, payload: Any) -> dict:
    brief = validate_brief(brief)
    if not isinstance(payload, dict) or payload.get("project_id") != brief["project_id"]:
        raise ValueError("Concepts must belong to the supplied brief")
    originality = compare(payload)
    concerns = []
    if originality["structural_gate"] == "fail":
        concerns.append("At least one concept pair lacks three meaningful structural distinctions, or a generic signal was flagged.")
    for concept in payload["concepts"]:
        if concept.get("risk"):
            concerns.append(f"{concept['id']}: {concept['risk']}")
    return {
        "project_id": brief["project_id"],
        "stage": "concept_only",
        "status": "UNVERIFIED_REQUIRES_HUMAN_REVIEW",
        "structural_gate": originality["structural_gate"],
        "structural_evidence": originality["pairwise"],
        "review_criteria": list(REVIEW_FIELDS),
        "ratings": {key: None for key in REVIEW_FIELDS},
        "hard_gates": {
            "scope_preserved": "not_tested",
            "truthful_assets": "not_tested",
            "accessibility_baseline": "not_tested",
            "functional_integrity": "not_tested",
            "structural_distinction": originality["structural_gate"],
            "evidence_integrity": "not_tested",
        },
        "known_concerns": concerns,
        "required_evidence": [
            "Validate all concept descriptions against the approved scope and verified assets.",
            "Human review of actual mobile and desktop compositions, not only structure tags.",
            "Keyboard, touch and reduced-motion testing if any concept is implemented.",
            "Independent reviewer ratings with concrete evidence before running tools/score.py.",
        ],
        "disclaimer": "This automated packet is NOT an AI visual critic; it only checks structured inputs and prepares prompts for human or external-model review.",
    }
