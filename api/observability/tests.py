from django.test import TestCase
from rest_framework.test import APIClient


class HealthTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_health_endpoint_exists(self):
        resp = self.client.get("/api/ops/health")
        self.assertIn(resp.status_code, (200, 503))
