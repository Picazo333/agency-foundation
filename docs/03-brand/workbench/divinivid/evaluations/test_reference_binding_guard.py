import unittest

from reference_binding_guard import check_binding


class ReferenceBindingGuardTests(unittest.TestCase):
    def setUp(self):
        self.record = {
            "call_id": "synthetic-call",
            "phase": "synthetic-phase",
            "executor": {"id": "synthetic-executor", "supports_image_references": True},
            "request": {
                "evidence_ref": "synthetic://request",
                "attached_reference_ids": ["approved-root"],
            },
            "approved_root_references": [
                {"id": "approved-root", "approval_ref": "synthetic://approval", "available": True}
            ],
            "rejected_descendant_ids": ["rejected-child"],
            "generated_descendants_excluded": True,
        }

    def test_bound_root_is_structurally_ready(self):
        self.assertEqual(check_binding(self.record), [])

    def test_available_but_not_attached_fails(self):
        self.record["request"]["attached_reference_ids"] = ["other"]
        self.assertTrue(any("absent" in x for x in check_binding(self.record)))

    def test_rejected_descendant_fails(self):
        self.record["request"]["attached_reference_ids"].append("rejected-child")
        self.assertTrue(any("rejected descendant" in x for x in check_binding(self.record)))

    def test_executor_without_image_binding_fails(self):
        self.record["executor"]["supports_image_references"] = False
        self.assertTrue(any("support image references" in x for x in check_binding(self.record)))

    def test_missing_request_evidence_fails(self):
        self.record["request"]["evidence_ref"] = ""
        self.assertTrue(any("evidence reference" in x for x in check_binding(self.record)))

    def test_malformed_attachment_fails_closed(self):
        self.record["request"]["attached_reference_ids"] = [{"id": "approved-root"}]
        self.assertTrue(any("distinct attached" in x for x in check_binding(self.record)))


if __name__ == "__main__":
    unittest.main()
