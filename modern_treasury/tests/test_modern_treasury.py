from unittest import TestCase
from unittest.mock import MagicMock

from modern_treasury.objects.request.internal_account import InternalAccountRequest
from modern_treasury.tests.utils import patch_obj_with_json

from ..modern_treasury import ModernTreasury


class ModernTreasuryTest(TestCase):
    def setUp(self):
        super().setUp()
        self.api = ModernTreasury.create("123", "321")

    @patch_obj_with_json(ModernTreasury, "_get", "modern_treasury/tests/fixtures/list_connections_response.json")
    def test__list_connections(self, mock_get):
        res = self.api.list_connections()
        self.assertEqual(len(res), 2)
    
    @patch_obj_with_json(ModernTreasury, "_post", "modern_treasury/tests/fixtures/internal_account_response.json")
    def test__create_internal_account(self, mock_post):
        request = InternalAccountRequest(
            connection_id="123",
            name="Levi is dead :(",
            party_name="lame party",
            currency="USD",
        )
        res = self.api.create_internal_account(request)
        self.assertEqual(res.json.get("object"), "internal_account")
    
    @patch_obj_with_json(ModernTreasury, "_get", "modern_treasury/tests/fixtures/list_connections_response.json")
    def test__get_connection(self, mock_get):
        res = self.api.get_connection_by_vendor(vendor_name="Gringotts Wizarding Bank")
        self.assertIsNotNone(res)
        res = self.api.get_connection_by_vendor(vendor_id="example1")
        self.assertIsNotNone(res)
        res = self.api.get_connection_by_vendor(vendor_id="random_string")
        self.assertIsNone(res)
    
    @patch_obj_with_json(ModernTreasury, "_get", "modern_treasury/tests/fixtures/list_counterparties_response.json")
    def test__get_counterparty_account_by_name(self, mock_get: MagicMock):
        res = self.api.get_counterparty_account_by_name("Adam Marshall")
        self.assertIsNotNone(res)
        res = self.api.get_counterparty_account_by_name("Levi Ackerman")
        self.assertIsNone(res) # :'(

    @patch_obj_with_json(ModernTreasury, "_get", "modern_treasury/tests/fixtures/list_counterparties_response.json")
    def test__list_counterparties(self, mock_get: MagicMock):
        res = self.api.list_counterparties()
        self.assertIsNotNone(res)
        self.assertDictEqual(mock_get.call_args[1]["params"], {"page": "1", "per_page": "100"})
        res = self.api.list_counterparties({"buyer_id": "2"})
        self.assertIsNotNone(res)
        self.assertDictEqual(mock_get.call_args[1]["params"], {"page": "1", "per_page": "100", "metadata[buyer_id]": "2"})
        
    @patch_obj_with_json(ModernTreasury, "_get", "modern_treasury/tests/fixtures/list_internal_accounts_response.json")
    def test__get_internal_accounts(self, mock_get):
        self.api.get_internal_accounts()
        self.assertIsNone(mock_get.call_args[1]["params"])
        self.api.get_internal_accounts(per_page="1000", page="2")
        self.assertDictEqual(mock_get.call_args[1]["params"], {"page": "2", "per_page": "1000"})
    
    @patch_obj_with_json(ModernTreasury, "_get", "modern_treasury/tests/fixtures/list_internal_accounts_response.json")
    def test__get_internal_account_by_id(self, mock_get):
        res = self.api.get_internal_account_by_id("12")
        self.assertIsNotNone(res)
        with self.assertRaises(Exception):
            self.api.get_internal_account_by_id()
    
    @patch_obj_with_json(ModernTreasury, "_get", "modern_treasury/tests/fixtures/list_internal_accounts_response.json")
    def test__list_payment_orders(self, mock_get):
        res = self.api.list_payment_orders()
        self.assertIsNotNone(res)
        res = self.api.list_payment_orders({"buyer_id": "2"})
        self.assertIsNotNone(res)
        self.assertDictEqual(mock_get.call_args[1]["params"], {"metadata[buyer_id]": "2"})

    @patch_obj_with_json(ModernTreasury, "_get", "modern_treasury/tests/fixtures/list_virtual_accounts_response.json")
    def test__list_virtual_accounts(self, mock_get):
        res = self.api.list_virtual_accounts()
        self.assertIsNotNone(res)
        res = self.api.list_virtual_accounts({"buyer_id": "2"})
        self.assertIsNotNone(res)
        self.assertDictEqual(mock_get.call_args[1]["params"], {"metadata[buyer_id]": "2"})
    
    @patch_obj_with_json(ModernTreasury, "_get", "modern_treasury/tests/fixtures/list_incoming_payment_details_respnose.json")
    def test__list_incoming_payment_detail(self, mock_get):
        res = self.api.list_incoming_payment_detail()
        self.assertIsNotNone(res)
        res = self.api.list_incoming_payment_detail("1234")
        self.assertIsNotNone(res)
        self.assertDictEqual(mock_get.call_args[1]["params"], {"virtual_account_id": "1234"})