"""Dependency-free regression tests for concept and originality tooling."""
from __future__ import annotations
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from creativecode.concepts import generate, validate_brief, STRUCTURE_KEYS, SUPPORTED_KINDS
from creativecode.originality import compare
from creativecode.critic import prepare

ROOT = Path(__file__).resolve().parent.parent


def sample(kind="portfolio"):
    return {
        "project_id": "example", "project_type": kind,
        "project_name": "Example", "audience": ["People looking for specific information"],
        "primary_goal": "Help people understand useful work",
        "primary_action": "Explore work", "constraints": {"production_changes": False},
        "content_items": [{"title": "Verified Item"}, {"title": "Other Item"}],
    }


class ConceptTests(unittest.TestCase):
    def test_generates_three_each_supported_kind(self):
        for kind in SUPPORTED_KINDS:
            with self.subTest(kind=kind):
                result = generate(sample(kind))
                self.assertEqual(len(result["concepts"]), 3)
                self.assertEqual(compare(result)["structural_gate"], "pass")

    def test_deterministic(self):
        self.assertEqual(generate(sample()), generate(sample()))

    def test_preserves_source_content_order(self):
        concepts = generate(sample())["concepts"]
        self.assertTrue(all(c["featured_content_in_source_order"] == ["Verified Item", "Other Item"] for c in concepts))

    def test_does_not_mutate_brief(self):
        brief = sample()
        initial = copy.deepcopy(brief)
        generate(brief)
        self.assertEqual(brief, initial)

    def test_approved_constraints_are_carried_through(self):
        result = generate(sample())
        self.assertTrue(all(c["project_constraints"]["production_changes"] is False for c in result["concepts"]))

    def test_disallows_empty_audience(self):
        b = sample(); b["audience"] = []
        with self.assertRaises(ValueError): validate_brief(b)

    def test_rejects_wrong_project_type(self):
        b = sample(); b["project_type"] = "whatever"
        with self.assertRaises(ValueError): generate(b)

    def test_rejects_invented_content_default(self):
        b = sample(); b["content_items"] = []
        with self.assertRaises(ValueError): generate(b)

    def test_rejects_missing_required_field(self):
        b = sample(); del b["primary_action"]
        with self.assertRaises(ValueError): generate(b)

    def test_metadata_distinguishes_patterns_from_ai(self):
        self.assertIn("no-llm", generate(sample())["generator"])

    def test_pairwise_diffs_at_least_three(self):
        result = compare(generate(sample()))
        self.assertEqual(len(result["pairwise"]), 3)
        self.assertTrue(all(p["different_dimension_count"] >= 3 for p in result["pairwise"]))

    def test_cosmetic_only_variation_is_rejected(self):
        data = generate(sample())
        one, two = data["concepts"][:2]
        for key in STRUCTURE_KEYS:
            two[key] = one[key]
        two["name"] = "Different color and rounded corners"
        self.assertEqual(compare(data)["structural_gate"], "fail")

    def test_one_distinct_dimension_not_enough(self):
        data = generate(sample())
        one, two = data["concepts"][:2]
        for key in STRUCTURE_KEYS[1:]: two[key] = one[key]
        self.assertEqual(compare(data)["structural_gate"], "fail")

    def test_no_two_identical_ids(self):
        data = generate(sample())
        data["concepts"][1]["id"] = data["concepts"][0]["id"]
        with self.assertRaises(ValueError): compare(data)

    def test_missing_structure_field_raises(self):
        data = generate(sample())
        del data["concepts"][0]["navigation_model"]
        with self.assertRaises(ValueError): compare(data)

    def test_known_ai_trope_warning(self):
        data = generate(sample())
        data["concepts"][0]["anti_patterns"] = ["decorative_emoji"]
        result = compare(data)
        self.assertEqual(result["structural_gate"], "fail")
        self.assertEqual(result["generic_pattern_warnings"][0]["signal"], "decorative_emoji")

    def test_critic_does_not_invent_ratings(self):
        b = sample()
        r = prepare(b, generate(b))
        self.assertEqual(r["status"], "UNVERIFIED_REQUIRES_HUMAN_REVIEW")
        self.assertTrue(all(value is None for value in r["ratings"].values()))
        self.assertEqual(r["hard_gates"]["accessibility_baseline"], "not_tested")

    def test_critic_passes_failed_structural_gate(self):
        b = sample()
        result = generate(b)
        for key in STRUCTURE_KEYS:
            result["concepts"][1][key] = result["concepts"][0][key]
        packet = prepare(b, result)
        self.assertEqual(packet["hard_gates"]["structural_distinction"], "fail")

    def test_critic_rejects_different_project(self):
        b = sample()
        result = generate(b); result["project_id"] = "other"
        with self.assertRaises(ValueError): prepare(b, result)

    def test_real_portfolio_pilot_is_structurally_distinct(self):
        b = json.loads((ROOT / "examples/portfolio_brief.json").read_text(encoding="utf-8"))
        c = generate(b)
        self.assertEqual(compare(c)["structural_gate"], "pass")
        self.assertEqual(c["concepts"][0]["featured_content_in_source_order"][0], "SellDibo")

    def test_cli_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            brief = Path(tmp) / "brief.json"
            brief.write_text(json.dumps(sample()), encoding="utf-8")
            concepts = Path(tmp) / "concepts.json"
            check = Path(tmp) / "check.json"
            for args in [["concepts", "--brief", str(brief), "--out", str(concepts)],
                         ["originality", "--concepts", str(concepts), "--out", str(check)]]:
                process = subprocess.run([sys.executable, "-m", "creativecode", *args], cwd=ROOT, capture_output=True, text=True)
                self.assertEqual(process.returncode, 0, process.stderr)
            self.assertEqual(json.loads(check.read_text())["structural_gate"], "pass")


if __name__ == "__main__":
    unittest.main()
