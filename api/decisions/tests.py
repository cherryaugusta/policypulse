from django.test import TestCase
from rest_framework.test import APIClient


class DecisionApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_submit_decision(self):
        payload = {
            "applicant_id": "applicant-token-123",
            "product": "loan_precheck",
            "features": {"income": 50000, "age": 30, "country": "GB"},
        }
        resp = self.client.post("/api/decisions/submit", payload, format="json")
        self.assertEqual(resp.status_code, 201)
        self.assertIn("decision_id", resp.data)
        self.assertEqual(resp.data["outcome"], "review")
