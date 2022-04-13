import json
import os
from unittest import TestCase
from unittest.mock import Mock

from modern_treasury.auth import Auth


FILE_PATH = os.path.dirname(os.path.abspath(__file__))


class AuthTestCase(TestCase):
    def setUp(self):
        with open(os.path.join(FILE_PATH, "./fixtures/payment_order_webhook_data.json"), "rb") as f:
            self.fixture_data = json.load(f)
            self.payment_order = json.dumps(self.fixture_data["payment_order_created"])
    def test__is_valid_webhook_request__is_valid(self):
        webhook_req = Mock()
        webhook_req.body = self.payment_order.encode("utf-8")
        webhook_req.headers = {
            "x-topic": "payment_order",
            "x-signature": "bb13fde71d81fdd910dbae7ce97e195e55556ff6a9fba00a33765a339de577df",
        }
        self.assertTrue(Auth.is_valid_webhook_request(webhook_req, "".encode("utf-8")))

    def test__is_valid_webhook_request__is_invalid(self):
        webhook_req = Mock()
        webhook_req.body = self.payment_order.encode("utf-8")
        webhook_req.headers = {
            "x-topic": "payment_order",
            "x-signature": "invalid",
        }
        self.assertTrue(not Auth.is_valid_webhook_request(webhook_req, "".encode("utf-8")))
