from dataclasses import dataclass
from typing import List

from .account_details import AccountDetailsRequest
from .address import AddressRequest
from .routing_details import RoutingDetailsRequest


@dataclass
class AccountRequest:
    address: AddressRequest
    account_type: str
    account_details_list: List[AccountDetailsRequest]
    routing_details_list: List[RoutingDetailsRequest]

    def to_json(self) -> dict:
        account_details = [account_details.to_json() for account_details in self.account_details_list]
        routing_details = [routing_details.to_json() for routing_details in self.routing_details_list]
        return {
            "party_address": self.address.to_json(),
            "account_type": self.account_type,
            "routing_details": routing_details,
            "account_details": account_details,
        }


