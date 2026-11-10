"""Structural concept comparison; heuristic checks do not prove originality."""

from __future__ import annotations
from itertools import combinations
from typing import Any
from .concepts import STRUCTURE_KEYS

MIN_DISTINCT_DIMENSIONS = 3
GENERIC_SIGNALS = {
    "three_equal_glowing_cards": "Repeated equal-sized glowing card rows are often generic without a task-specific reason.",
    "decorative_emoji": "Decorative emoji in controls or navigation should be replaced with coherent iconography.",
    "color_swap_only": "Changing only color or typography does not create a separate concept.",
    "unnecessary_scroll_animation": "Decorative motion can distract from primary actions and harm accessibility.",
    "fabricated_proof": "Invented statistics, testimonials or screenshots are unacceptable.",
}


def compare(payload: Any) -> dict:
    if not isinstance(payload, dict) or not isinstance(payload.get("concepts"), list):
        raise ValueError("Concept input must have a concepts array")
    concepts = payload["concepts"]
    if len(concepts) < 2:
        raise ValueError("At least two concepts are needed for comparison")
    ids: set[str] = set()
    for concept in concepts:
        if not isinstance(concept, dict):
            raise ValueError("Each concept must be a JSON object")
        cid = concept.get("id")
        if not isinstance(cid, str) or not cid.strip() or cid in ids:
            raise ValueError("Concept IDs must be distinct nonempty strings")
        ids.add(cid)
        for key in STRUCTURE_KEYS:
            if not isinstance(concept.get(key), str) or not concept[key].strip():
                raise ValueError(f"Concept {cid} lacks a nonempty {key}")
    pairs = []
    for left, right in combinations(concepts, 2):
        differences = [key for key in STRUCTURE_KEYS if left[key].strip().casefold() != right[key].strip().casefold()]
        pairs.append({
            "left": left["id"], "right": right["id"],
            "different_dimensions": differences, "different_dimension_count": len(differences),
            "passes_structural_distinction": len(differences) >= MIN_DISTINCT_DIMENSIONS,
        })
    warnings = []
    for c in concepts:
        for flag in c.get("anti_patterns", []):
            if flag in GENERIC_SIGNALS:
                warnings.append({"concept_id": c["id"], "signal": flag, "reason": GENERIC_SIGNALS[flag]})
    passed = all(pair["passes_structural_distinction"] for pair in pairs) and not warnings
    return {
        "project_id": payload.get("project_id", "unknown"),
        "method": "declared-structure-heuristic",
        "not_a_proof_of_originality": True,
        "pairwise": pairs, "generic_pattern_warnings": warnings,
        "structural_gate": "pass" if passed else "fail",
        "required_different_dimensions": MIN_DISTINCT_DIMENSIONS,
        "note": "Compares declared architecture labels, not screenshots or internet-wide designs. Human visual review remains required.",
    }
