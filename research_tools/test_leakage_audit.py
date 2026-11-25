import unittest

from leakage_audit import audit_rows


class LeakageAuditTests(unittest.TestCase):
    def test_group_crossing_splits_is_leakage(self):
        rows = [
            {"sample_id": "a", "split": "train", "group_id": "tree-1"},
            {"sample_id": "b", "split": "test", "group_id": "tree-1"},
        ]
        report = audit_rows(rows)
        self.assertFalse(report["passed"])
        self.assertEqual(report["cross_split_leakage"][0]["type"], "group_id_cross_split")

    def test_same_group_within_one_split_passes(self):
        rows = [
            {"sample_id": "a", "split": "train", "group_id": "tree-1"},
            {"sample_id": "b", "split": "train", "group_id": "tree-1"},
            {"sample_id": "c", "split": "test", "group_id": "tree-2"},
        ]
        self.assertTrue(audit_rows(rows)["passed"])

    def test_duplicate_hash_across_splits_is_leakage(self):
        rows = [
            {"sample_id": "a", "split": "train", "sha256": "ABC"},
            {"sample_id": "b", "split": "test", "sha256": "abc"},
        ]
        self.assertFalse(audit_rows(rows)["passed"])

    def test_duplicate_sample_id_is_error(self):
        rows = [
            {"sample_id": "a", "split": "train"},
            {"sample_id": "a", "split": "test"},
        ]
        self.assertEqual(audit_rows(rows)["errors"][0]["type"], "duplicate_sample_id")


if __name__ == "__main__":
    unittest.main()
