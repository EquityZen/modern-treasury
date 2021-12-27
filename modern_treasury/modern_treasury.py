from typing import Optional, List

import requests
from requests.auth import HTTPBasicAuth

from modern_treasury import AccountDetailsResponse, AccountDetailsRequest, PaymentOrderResponse
from modern_treasury.objects.exceptions import ModernTreasuryException
from modern_treasury.objects.request.counterparty import CounterPartyRequest
from modern_treasury.objects.request.expected_payment import ExpectedPaymentRequest
from modern_treasury.objects.request.external_account import ExternalAccountRequest
from modern_treasury.objects.request.incoming_payment_detail import IncomingPaymentDetailRequest
from modern_treasury.objects.request.payment_order import PaymentOrderRequest
from modern_treasury.objects.request.routing_details import RoutingDetailsRequest
from modern_treasury.objects.request.virtual_account import VirtualAccountRequest
from modern_treasury.objects.response.counterparty import CounterPartyResponse
from modern_treasury.objects.response.expected_payment import ExpectedPaymentResponse
from modern_treasury.objects.response.external_account import ExternalAccountResponse
from modern_treasury.objects.response.incoming_payment_detail import IncomingPaymentDetailResponse
from modern_treasury.objects.response.internal_account import InternalAccountResponse

from modern_treasury.objects.response.routing_details import RoutingDetailsResponse
from modern_treasury.objects.response.virtual_account import VirtualAccountResponse

INTERNAL_ACCOUNT_URL = 'https://app.moderntreasury.com/api/internal_accounts'
COUNTER_PARTIES_URL = 'https://app.moderntreasury.com/api/counterparties'
EXPECTED_PAYMENTS_URL = 'https://app.moderntreasury.com/api/expected_payments'
PAYMENT_ORDER_URL = 'https://app.moderntreasury.com/api/payment_orders'
VIRTUAL_ACCOUNT_URL = 'https://app.moderntreasury.com/api/virtual_accounts'
EXTERNAL_ACCOUNT_URL = 'https://app.moderntreasury.com/api/external_accounts'

INCOMING_PAYMENT_DETAIL_URL = 'https://app.moderntreasury.com/api/simulations/incoming_payment_details/create_async'


class ModernTreasury:
    def create(organization_id:str, api_key:str):
        return ModernTreasury(organization_id=organization_id, api_key=api_key)

    def __init__(self, organization_id: str, api_key: str):
        self.organization_id = organization_id
        self.api_key = api_key
        self.http_basic_auth = HTTPBasicAuth(username=self.organization_id, password=self.api_key)
        self.headers = {"Content-Type": "application/json"}

    def _post(self, url:str, payload: dict, key: str = None) -> dict:
        headers = {**self.headers, "Idempotency-Key": key} if key else self.headers
        response = requests.post(url=url,
                                 auth=self.http_basic_auth,
                                 headers=headers,
                                 json=payload)
        if not response.ok:
            raise ModernTreasuryException(response.status_code, response.reason, url, response.json())
        return response.json()

    def _get(self, url:str, params = None) -> dict:
        response = requests.get(url=url,
                                auth=self.http_basic_auth,
                                headers=self.headers,
                                params=params)
        if not response.ok:
            raise ModernTreasuryException(response.status_code, response.reason, url, response.json())
        return response.json()

    def _patch(self, url:str, payload: dict) -> dict:
        response = requests.request("PATCH",
                                    url=url,
                                    json=payload,
                                    headers=self.headers,
                                    auth=self.http_basic_auth)
        if not response.ok:
            raise ModernTreasuryException(response.status_code, response.reason, url, response)
        return response.json()

    def _delete(self, url:str) -> dict:
        response = requests.request("DELETE",
                                    url=url,
                                    headers=self.headers,
                                    auth=self.http_basic_auth)
        if not response.ok:
            raise ModernTreasuryException(response.status_code, response.reason, url, response)

    # Counter Parties
    def get_counter_parties(self):
        return self._get(url=COUNTER_PARTIES_URL)

    def get_counter_party_account_by_name(self, name) -> Optional[CounterPartyResponse]:
        for account in self.get_counter_parties():
            mt_account = CounterPartyResponse(account)
            if mt_account.name == name:
                return mt_account
        return None

    def update_counterparty(self, counter_party_request: CounterPartyRequest, counter_party_id:str):
        payload = counter_party_request.to_json()
        self._patch(url=f'{COUNTER_PARTIES_URL}/{counter_party_id}',
                    payload=payload)

    def list_counterparties(self, metadata: dict=None) -> List[Optional[CounterPartyResponse]]:
        querystring = {'page': '1', 'per_page': '100'}
        if metadata:
            for key, value in metadata.items():
                querystring[f'metadata[{str(key)}]'] = str(value)

        try:
            response = self._get(url=COUNTER_PARTIES_URL, params=querystring)
            return [CounterPartyResponse(counterparty) for counterparty in response]
        except:
            return []

    def delete_counterparty_by_id(self, id:str) -> bool:
        return self._delete(url=f'{COUNTER_PARTIES_URL}/{id}')

    def get_counterparty_account_by_id(self, id:str) -> CounterPartyResponse:
        return CounterPartyResponse(self._get(url=f'{COUNTER_PARTIES_URL}/{id}'))

    def create_counterparty_account(self, counterparty_request: CounterPartyRequest, key: str = None) -> CounterPartyResponse:
        return CounterPartyResponse(self._post(url=COUNTER_PARTIES_URL, payload=counterparty_request.to_json()), key=key)

    # external account
    def update_external_account(self, external_account_request: ExternalAccountRequest,
                                external_account_id:str) -> ExternalAccountResponse:
        payload = external_account_request.to_json()
        result = self._patch(url=f'{EXTERNAL_ACCOUNT_URL}/{external_account_id}',
                             payload=payload)
        if result:
            return ExternalAccountResponse(result)
        return None

    # account details
    def delete_account_details(self, external_account_id:str, account_details_id:str):
        url = f'{EXTERNAL_ACCOUNT_URL}/{external_account_id}/account_details/{account_details_id}'
        result = self._delete(url=url)
        return result

    def create_account_details(self, account_details: AccountDetailsRequest,
                               external_account_id: str,
                               key: str = None) -> AccountDetailsResponse:
        url = f'{EXTERNAL_ACCOUNT_URL}/{external_account_id}/account_details'
        payload = account_details.to_json()
        return AccountDetailsResponse(self._post(url=url, payload=payload, key=key))

    # routing details
    def get_routing_details_by_id(self, external_account_id, routing_details_id):
        url = f'{EXTERNAL_ACCOUNT_URL}/{external_account_id}/routing_details/{routing_details_id}'
        return self._get(url=url)

    def delete_routing_details(self, external_account_id:str, routing_details_id:str):
        url = f'{EXTERNAL_ACCOUNT_URL}/{external_account_id}/routing_details/{routing_details_id}'
        result = self._delete(url=url)
        return result

    def create_routing_details(self, routing_details: RoutingDetailsRequest,
                               external_account_id: str,
                               key: str = None) -> RoutingDetailsResponse:
        url = f'{EXTERNAL_ACCOUNT_URL}/{external_account_id}/routing_details'
        payload = routing_details.to_json()
        return RoutingDetailsResponse(self._post(url=url, payload=payload, key=key))

    # Internal Accounts
    def get_internal_accounts(self):
        result = self._get(url=INTERNAL_ACCOUNT_URL)

        internal_accounts = []
        for account in result:
            internal_accounts.append(InternalAccountResponse(account))
        return internal_accounts

    def get_internal_account_by_id(self, id:str) -> Optional[InternalAccountResponse]:
        if id:
            result = self._get(url=f'{INTERNAL_ACCOUNT_URL}/{id}')
            return InternalAccountResponse(result)
        else:
            raise Exception("id cannot be an empty string")

    # External Accounts
    def create_external_account(self, external_account_request: ExternalAccountRequest, key: str = None):
        response = self._post(url=EXTERNAL_ACCOUNT_URL, payload=external_account_request.to_json(), key=key)
        return ExpectedPaymentResponse(response)

    def delete_external_account(self, external_account_id:str):
        url = f'{EXTERNAL_ACCOUNT_URL}/{external_account_id}'
        result = self._delete(url=url)
        return result

    # Expected Payments
    def create_expected_payment(self, expected_payment_request: ExpectedPaymentRequest, key: str = None) -> ExpectedPaymentResponse:
        response = self._post(url=EXPECTED_PAYMENTS_URL, payload=expected_payment_request.to_json(), key=key)
        return ExpectedPaymentResponse(response)

    def get_expected_payment_by_id(self, id:str) -> Optional[ExpectedPaymentResponse]:
        result = requests.get(url=f'{EXPECTED_PAYMENTS_URL}/{id}', auth=self.http_basic_auth)
        return ExpectedPaymentResponse(result.json())

    def update_expected_payment(self, id:str, expected_payment_request: ExpectedPaymentRequest) -> ExpectedPaymentResponse:
        response = self._patch(url=f'{EXPECTED_PAYMENTS_URL}/{id}', payload=expected_payment_request.to_json())
        return ExpectedPaymentResponse(response)

    # Payment Orders
    def create_payment_order(self, payment_order_request: PaymentOrderRequest, key: str = None) -> PaymentOrderResponse:
        response = self._post(url=PAYMENT_ORDER_URL, payload=payment_order_request.to_json(), key=key)
        return PaymentOrderResponse(response)

    def get_payment_order(self):
        result = self._get(url=f'{PAYMENT_ORDER_URL}/{id}')
        return ExpectedPaymentResponse(result.json())

    # Virtual Account
    def create_virtual_account(self, virtual_account_request: VirtualAccountRequest, key: str = None):
        response = self._post(url=VIRTUAL_ACCOUNT_URL,
                              payload=virtual_account_request.to_json(),
                              key=key)
        return VirtualAccountResponse(response)

    def get_virtual_account_by_id(self, id:str):
        result = requests.get(url=f'{VIRTUAL_ACCOUNT_URL}/{id}', auth=self.http_basic_auth)
        return VirtualAccountResponse(result.json())

    def post_incoming_payment_detail(self, incoming_payment_detail_request: IncomingPaymentDetailRequest, key: str = None)\
            -> IncomingPaymentDetailResponse:
        response = self._post(url=INCOMING_PAYMENT_DETAIL_URL,
                              payload=incoming_payment_detail_request.to_json(),
                              key=key)
        return IncomingPaymentDetailResponse(response)
