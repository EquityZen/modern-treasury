from .address import AddressRequest
from .account_details import AccountDetailsRequest
from .routing_details import RoutingDetailsRequest
from typing import List


class ExternalAccountRequest():
    def __init__(self,
                 counterparty_id: str,
                 account_details: List[AccountDetailsRequest] = None,
                 routing_details: List[RoutingDetailsRequest] = None,
                 account_type:str = None,
                 party_address:AddressRequest = None,
                 idempotency_key:str = None):
        self.counterparty_id = counterparty_id
        self.account_details = account_details if account_details else []
        self.routing_details = routing_details if routing_details else []
        self.account_type = account_type
        self.party_address = party_address
        self.idempotency_key  = f"external_account_{idempotency_key}" if idempotency_key else None

    def to_json(self):
        account_details_json = [account_detail.to_json() for account_detail in self.account_details]
        routing_details_json = [routing_detail.to_json() for routing_detail in self.routing_details]
        result = {
            'counterparty_id': self.counterparty_id,
            'account_details': account_details_json,
            'routing_details': routing_details_json,
        }
        if self.account_type:
            result['account_type'] = self.account_type
        if self.party_address:
            result['party_address'] = self.party_address.to_json()

        return result
