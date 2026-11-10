#!/usr/bin/env python3
"""CreativeCode V1 scorecard. Python stdlib only; never claims visual verification."""

from __future__ import annotations
import json
import math
import sys
from pathlib import Path

WEIGHTS = {
    "originality": 20, "strategy": 15, "hierarchy": 15,
    "typography": 10, "composition": 10, "usability": 10,
    "responsive": 10, "motion": 5, "engineering": 5,
}
GATES = (
    "scope_preserved", "truthful_assets", "accessibility_baseline",
    "functional_integrity", "structural_distinction", "evidence_integrity",
)
assert sum(WEIGHTS.values()) == 100


def evaluate(data: dict) -> dict:
    if not isinstance(data, dict):
        raise ValueError("Review input must be a JSON object")
    ratings = data.get("ratings", {})
    gates = data.get("gates", {})
    if not isinstance(ratings, dict):
        raise ValueError("ratings must be a JSON object")
    if not isinstance(gates, dict):
        raise ValueError("gates must be a JSON object")
    if set(ratings) != set(WEIGHTS):
        raise ValueError(f"Ratings must have exactly these keys: {', '.join(WEIGHTS)}")
    if set(gates) != set(GATES):
        raise ValueError(f"Gates must have exactly these keys: {', '.join(GATES)}")
    for key, value in ratings.items():
        if (isinstance(value, bool) or not isinstance(value, (int, float))
                or not math.isfinite(value) or not 0 <= value <= 5):
            raise ValueError(f"Rating {key!r} must be a number between 0 and 5")
    for key, value in gates.items():
        if not isinstance(value, str) or value not in ("pass", "fail", "not_tested"):
            raise ValueError(f"Gate {key!r} must be pass, fail or not_tested")
    score = round(sum(ratings[key] * weight / 5 for key, weight in WEIGHTS.items()), 2)
    if "fail" in gates.values():
        status = "BLOCKED"
    elif "not_tested" in gates.values():
        status = "UNVERIFIED"
    elif ratings["originality"] < 3.5 or ratings["usability"] < 3:
        status = "REWORK"
    elif score >= 85:
        status = "CANDIDATE_FOR_HUMAN_APPROVAL"
    elif score >= 70:
        status = "REVISE"
    else:
        status = "REWORK"
    return {"project": data.get("project", "unknown"), "score": score,
            "status": status, "unverified_gates": [k for k in GATES if gates[k] == "not_tested"],
            "failed_gates": [k for k in GATES if gates[k] == "fail"],
            "note": "Recorded ratings are reviewer judgments, not automated design proof."}


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 tools/score.py path/to/review.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        print(json.dumps(evaluate(data), ensure_ascii=False, indent=2))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
