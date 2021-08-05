from typing import Optional

import requests
from requests.auth import HTTPBasicAuth

from modern_treasury.objects.request.counterparty import CounterPartyRequest
from modern_treasury.objects.request.expected_payment import ExpectedPaymentRequest
from modern_treasury.objects.request.payment_order import PaymentOrderRequest
from modern_treasury.objects.request.virtual_account import VirtualAccountRequest
from modern_treasury.objects.response.counterparty import CounterPartyResponse
from modern_treasury.objects.response.expected_response import ExpectedPaymentResponse
from modern_treasury.objects.response.internal_account import InternalAccountResponse
from modern_treasury.objects.response.payment import PaymentOrderResponse
from modern_treasury.objects.response.virtual_account import VirtualAccountResponse

INTERNAL_ACCOUNT_URL = 'https://app.moderntreasury.com/api/internal_accounts'
COUNTER_PARTIES_URL = 'https://app.moderntreasury.com/api/counterparties'
EXPECTED_PAYMENTS_URL = 'https://app.moderntreasury.com/api/expected_payments'
PAYMENT_ORDER_URL = 'https://app.moderntreasury.com/api/payment_orders'
VIRTUAL_ACCOUNT_URL = 'https://app.moderntreasury.com/api/virtual_accounts'


class ModernTreasury:
    def create(organization_id:str, api_key:str):
        return ModernTreasury(organization_id=organization_id, api_key=api_key)

    def __init__(self, organization_id: str, api_key: str):
        self.organization_id = organization_id
        self.api_key = api_key
        self.http_basic_auth = HTTPBasicAuth(username=self.organization_id, password=self.api_key)

    def _post(self, url:str, payload: dict) -> dict:
        response = requests.post(url=url,
                                 auth=self.http_basic_auth,
                                 headers={'Content-Type': 'application/json'},
                                 json=payload)
        return response.json()



    # Counter Parties
    def get_counter_parties(self):
        response= requests.get(COUNTER_PARTIES_URL, auth=self.http_basic_auth)
        return response.json()

    def get_counter_party_account_by_name(self, name) -> Optional[CounterPartyResponse]:
        for account in self.get_counter_parties():
            mt_account = CounterPartyResponse(account)
            if mt_account.name == name:
                return mt_account
        return None

    def get_counter_party_account_by_id(self, id:str) -> Optional[CounterPartyResponse]:
        result = requests.get(url=f'{COUNTER_PARTIES_URL}/{id}', auth=self.http_basic_auth)
        if result.ok:
            return CounterPartyResponse(result.json())
        return None

    def create_counter_party_account(self, counter_party_request: CounterPartyRequest) -> CounterPartyResponse:
        response = self._post(url=COUNTER_PARTIES_URL, payload=counter_party_request.to_json())
        counter_party_response = CounterPartyResponse(response)
        return counter_party_response

    # Internal Accounts
    def get_internal_accounts(self):
        response = requests.get(url=INTERNAL_ACCOUNT_URL, auth=self.http_basic_auth)
        result = response.json()

        internal_accounts = []
        for account in result:
            internal_accounts.append(InternalAccountResponse(account))
        return internal_accounts

    def get_internal_account_by_id(self, id:str) -> Optional[InternalAccountResponse]:
        result = requests.get(url=f'{INTERNAL_ACCOUNT_URL}/{id}', auth=self.http_basic_auth)
        if result.ok:
            return InternalAccountResponse(result.json())
        return None

    # Expected Payments
    def create_expected_payment(self, expected_payment_request: ExpectedPaymentRequest) -> Optional[ExpectedPaymentResponse]:
        response = self._post(url=EXPECTED_PAYMENTS_URL, payload=expected_payment_request.to_json())
        if response:
            return ExpectedPaymentResponse(response)
        return None

    def get_expected_payment_by_id(self, id:str) -> Optional[ExpectedPaymentResponse]:
        result = requests.get(url=f'{EXPECTED_PAYMENTS_URL}/{id}', auth=self.http_basic_auth)
        if result.ok:
            return ExpectedPaymentResponse(result.json())
        return None

    def update_expected_payment(self, id:str, expected_payment_request: ExpectedPaymentRequest) -> ExpectedPaymentResponse:
        headers = {"Content-Type": "application/json"}
        response = requests.request("PATCH", f'{EXPECTED_PAYMENTS_URL}/{id}',
                                    payload=expected_payment_request.to_json(),
                                    headers=headers)
        return ExpectedPaymentResponse(response)

    # Payment Orders
    def create_payment_order(self, payment_order_request: PaymentOrderRequest) -> Optional[PaymentOrderResponse]:
        response = self._post(url=PAYMENT_ORDER_URL, payload=payment_order_request.to_json())
        if response:
            return PaymentOrderResponse(response)
        return None

    def get_payment_order(self):
        result = requests.get(url=f'{PAYMENT_ORDER_URL}/{id}', auth=self.http_basic_auth)
        if result.ok:
            return ExpectedPaymentResponse(result.json())
        return None

    # Virtual Account
    def create_virtual_account(self, virtual_account_request: VirtualAccountRequest):
        response = self._post(url=VIRTUAL_ACCOUNT_URL,
                              payload=virtual_account_request.to_json())
        if response:
            return VirtualAccountResponse(response)
        return None

    def get_virtual_account_by_id(self, id:str):
        result = requests.get(url=f'{VIRTUAL_ACCOUNT_URL}/{id}', auth=self.http_basic_auth)
        if result.ok:
            return VirtualAccountResponse(result.json())
        return None

    # TODO support idempotency


# TODO: make singleton
SANDBOX_KEY = "test-CxfzxGrJqmNtoUmmyQyXyDR85yi8dGP33zmeYLfzCzuka2D6UpiJLAMscjrX1wPj"
ORGANIZATION_ID = "4aedefda-78df-4cfc-a3e5-42c2ba3f7e9a"

sandbox_modern_treasury = ModernTreasury(organization_id=ORGANIZATION_ID, api_key=SANDBOX_KEY)
