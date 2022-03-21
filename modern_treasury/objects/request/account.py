from typing import List

from .account_details import AccountDetailsRequest
from .address import AddressRequest
from .routing_details import RoutingDetailsRequest


class AccountRequest:
    def __init__(self,
                 account_type:str,
                 account_details_list: List[AccountDetailsRequest],
                 routing_details_list: List[RoutingDetailsRequest],
                 address: AddressRequest = None):
        self.address = address
        self.account_type = account_type
        self.account_details_list = account_details_list
        self.routing_details_list = routing_details_list

    def to_json(self) -> dict:
        account_details = [account_details.to_json() for account_details in self.account_details_list]
        routing_details = [routing_details.to_json() for routing_details in self.routing_details_list]
        party_address = self.address.to_json() if self.address else None
        return {
            "party_address": party_address,
            "account_type": self.account_type,
            "routing_details": routing_details,
            "account_details": account_details,
        }


