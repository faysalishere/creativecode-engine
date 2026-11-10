import unittest
import math
from score import evaluate, WEIGHTS, GATES


def payload(rating=5, gate="pass"):
    return {"project": "test", "ratings": {k: rating for k in WEIGHTS},
            "gates": {k: gate for k in GATES}}


class ScoreTests(unittest.TestCase):
    def test_max_pass(self):
        result = evaluate(payload())
        self.assertEqual(result["score"], 100)
        self.assertEqual(result["status"], "CANDIDATE_FOR_HUMAN_APPROVAL")

    def test_average_rework(self):
        self.assertEqual(evaluate(payload(3))["status"], "REWORK")

    def test_critical_fail_overrides_high_score(self):
        data = payload()
        data["gates"]["evidence_integrity"] = "fail"
        self.assertEqual(evaluate(data)["status"], "BLOCKED")

    def test_unknown_gate_is_unverified(self):
        data = payload()
        data["gates"]["functional_integrity"] = "not_tested"
        self.assertEqual(evaluate(data)["status"], "UNVERIFIED")

    def test_low_originality_disqualifies(self):
        data = payload()
        data["ratings"]["originality"] = 3
        self.assertEqual(evaluate(data)["status"], "REWORK")

    def test_rating_out_of_range(self):
        data = payload()
        data["ratings"]["motion"] = 6
        with self.assertRaises(ValueError):
            evaluate(data)

    def test_missing_key(self):
        data = payload()
        del data["ratings"]["composition"]
        with self.assertRaises(ValueError):
            evaluate(data)

    def test_not_a_document_rejected(self):
        with self.assertRaises(ValueError):
            evaluate([])

    def test_wrong_rating_type_rejected(self):
        data = payload()
        data["ratings"] = None
        with self.assertRaises(ValueError):
            evaluate(data)

    def test_wrong_gate_type_rejected(self):
        data = payload()
        data["gates"] = []
        with self.assertRaises(ValueError):
            evaluate(data)

    def test_nan_rejected(self):
        data = payload()
        data["ratings"]["motion"] = math.nan
        with self.assertRaises(ValueError):
            evaluate(data)

    def test_infinity_rejected(self):
        data = payload()
        data["ratings"]["strategy"] = math.inf
        with self.assertRaises(ValueError):
            evaluate(data)

    def test_invalid_gate_value_rejected(self):
        data = payload()
        data["gates"]["functional_integrity"] = "probably"
        with self.assertRaises(ValueError):
            evaluate(data)

    def test_revision_score_band(self):
        self.assertEqual(evaluate(payload(4))["status"], "REVISE")

    def test_not_tested_and_fail_status_priority(self):
        data = payload()
        data["gates"]["scope_preserved"] = "not_tested"
        data["gates"]["evidence_integrity"] = "fail"
        self.assertEqual(evaluate(data)["status"], "BLOCKED")

    def test_bool_rejected(self):
        data = payload()
        data["ratings"]["motion"] = True
        with self.assertRaises(ValueError):
            evaluate(data)


if __name__ == '__main__':
    unittest.main()
