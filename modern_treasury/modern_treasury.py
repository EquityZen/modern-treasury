from typing import Optional, List

import requests
from requests.auth import HTTPBasicAuth

from modern_treasury import AccountDetailsResponse, AccountDetailsRequest
from modern_treasury.objects.request.counterparty import CounterPartyRequest
from modern_treasury.objects.request.expected_payment import ExpectedPaymentRequest
from modern_treasury.objects.request.external_account import ExternalAccountRequest
from modern_treasury.objects.request.payment_order import PaymentOrderRequest
from modern_treasury.objects.request.routing_details import RoutingDetailsRequest
from modern_treasury.objects.request.virtual_account import VirtualAccountRequest
from modern_treasury.objects.response.counterparty import CounterPartyResponse
from modern_treasury.objects.response.expected_payment import ExpectedPaymentResponse
from modern_treasury.objects.response.external_account import ExternalAccountResponse
from modern_treasury.objects.response.internal_account import InternalAccountResponse
from modern_treasury.objects.response.payment import PaymentOrderResponse
from modern_treasury.objects.response.routing_details import RoutingDetailsResponse
from modern_treasury.objects.response.virtual_account import VirtualAccountResponse

INTERNAL_ACCOUNT_URL = 'https://app.moderntreasury.com/api/internal_accounts'
COUNTER_PARTIES_URL = 'https://app.moderntreasury.com/api/counterparties'
EXPECTED_PAYMENTS_URL = 'https://app.moderntreasury.com/api/expected_payments'
PAYMENT_ORDER_URL = 'https://app.moderntreasury.com/api/payment_orders'
VIRTUAL_ACCOUNT_URL = 'https://app.moderntreasury.com/api/virtual_accounts'
EXTERNAL_ACCOUNT_URL = 'https://app.moderntreasury.com/api/external_accounts'


class ModernTreasury:
    def create(organization_id:str, api_key:str):
        return ModernTreasury(organization_id=organization_id, api_key=api_key)

    def __init__(self, organization_id: str, api_key: str):
        self.organization_id = organization_id
        self.api_key = api_key
        self.http_basic_auth = HTTPBasicAuth(username=self.organization_id, password=self.api_key)
        self.headers = {"Content-Type": "application/json"}

    def _post(self, url:str, payload: dict) -> dict:
        response = requests.post(url=url,
                                 auth=self.http_basic_auth,
                                 headers=self.headers,
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

    def update_counterparty(self, counter_party_request: CounterPartyRequest, counter_party_id:str):
        payload = counter_party_request.to_json()
        requests.request("PATCH",
                         url=f'{COUNTER_PARTIES_URL}/{counter_party_id}',
                         json=payload,
                         headers=self.headers,
                         auth=self.http_basic_auth)

    def list_counterparties(self, metadata: dict=None) -> List[Optional[CounterPartyResponse]]:
        querystring = {'page': '1', 'per_page': '100'}
        if metadata:
            for key, value in metadata.items():
                querystring[f'metadata[{str(key)}]'] = str(value)
        response = requests.get(COUNTER_PARTIES_URL, auth=self.http_basic_auth, params=querystring)

        if response.ok:
            return [CounterPartyResponse(counterparty) for counterparty in response.json()]
        return []

    def delete_counterparty_by_id(self, id:str) -> bool:
        result = requests.request("DELETE", f'{COUNTER_PARTIES_URL}/{id}', auth=self.http_basic_auth)
        return True if result.ok else False

    def get_counterparty_account_by_id(self, id:str) -> Optional[CounterPartyResponse]:
        result = requests.get(url=f'{COUNTER_PARTIES_URL}/{id}', auth=self.http_basic_auth)
        if result.ok:
            return CounterPartyResponse(result.json())
        return None

    def create_counterparty_account(self, counterparty_request: CounterPartyRequest) -> Optional[CounterPartyResponse]:
        response = self._post(url=COUNTER_PARTIES_URL, payload=counterparty_request.to_json())
        if response:
            return CounterPartyResponse(response)
        return None

    # external account
    def update_external_account(self, external_account_request: ExternalAccountRequest,
                                external_account_id:str) -> Optional[ExternalAccountResponse]:
        payload = external_account_request.to_json()
        result = requests.request("PATCH",
                                  url=f'{EXTERNAL_ACCOUNT_URL}/{external_account_id}',
                                  json=payload,
                                  headers=self.headers,
                                  auth=self.http_basic_auth)
        if result:
            return ExternalAccountResponse(result.json())
        return None

    # account details
    def delete_account_details(self, external_account_id:str, account_details_id:str):
        url = f'{EXTERNAL_ACCOUNT_URL}/{external_account_id}/account_details/{account_details_id}'
        result = requests.request("DELETE",
                                  url=url,
                                  headers=self.headers,
                                  auth=self.http_basic_auth)
        return result

    def create_account_details(self, account_details: AccountDetailsRequest,
                               external_account_id: str) -> Optional[AccountDetailsResponse]:
        url = f'{EXTERNAL_ACCOUNT_URL}/{external_account_id}/account_details'
        payload = account_details.to_json()
        result = self._post(url=url, payload=payload)
        if result:
            return AccountDetailsResponse(result)
        return None

    # routing details
    def get_routing_details_by_id(self, external_account_id, routing_details_id):
        url = f'{EXTERNAL_ACCOUNT_URL}/{external_account_id}/routing_details/{routing_details_id}'
        response= requests.get(url=url, auth=self.http_basic_auth)
        return response.json()

    def delete_routing_details(self, external_account_id:str, routing_details_id:str):
        url = f'{EXTERNAL_ACCOUNT_URL}/{external_account_id}/routing_details/{routing_details_id}'
        result = requests.request("DELETE",
                                  url=url,
                                  auth=self.http_basic_auth)
        return result

    def create_routing_details(self, routing_details: RoutingDetailsRequest,
                               external_account_id: str) -> Optional[RoutingDetailsResponse]:
        url = f'{EXTERNAL_ACCOUNT_URL}/{external_account_id}/routing_details'
        payload = routing_details.to_json()
        result = self._post(url=url, payload=payload)
        if result:
            return RoutingDetailsResponse(result)
        return None

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
