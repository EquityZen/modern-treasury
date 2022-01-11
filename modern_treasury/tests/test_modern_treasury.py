import json
from unittest import TestCase
from unittest.mock import patch

from modern_treasury.objects.request.internal_account import InternalAccountRequest

from ..modern_treasury import ModernTreasury


class ModernTreasuryTest(TestCase):
    def setUp(self):
        super().setUp()
        self.api = ModernTreasury.create("123", "321")

    @patch.object(ModernTreasury, "_get")
    def test__list_connections(self, mock_get):
        with open("modern_treasury/tests/fixtures/list_connections_response.json", "rb") as f:
            mock_get.return_value = json.load(f)
            res = self.api.list_connections()
            self.assertEqual(len(res), 2)
    
    @patch.object(ModernTreasury, "_post")
    def test__create_internal_account(self, mock_post):
        request = InternalAccountRequest(
            connection_id="123",
            name="Levi is dead :(",
            party_name="lame party",
            currency="USD",
        )
        with open("modern_treasury/tests/fixtures/internal_account_response.json", "rb") as f:
            mock_post.return_value = json.load(f)
            res = self.api.create_internal_account(request)
            self.assertEqual(res.json.get("object"), "internal_account")
    
    @patch.object(ModernTreasury, "_get")
    def test__get_connection(self, mock_get):
        with open("modern_treasury/tests/fixtures/list_connections_response.json", "rb") as f:
            mock_get.return_value = json.load(f)
            res = self.api.get_connection(vendor_name="Gringotts Wizarding Bank")
            self.assertIsNotNone(res)
            res = self.api.get_connection(vendor_id="example1")
            self.assertIsNotNone(res)
            res = self.api.get_connection(vendor_id="random_string")
            self.assertIsNone(res)