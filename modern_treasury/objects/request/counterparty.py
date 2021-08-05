import json
from typing import List

from modern_treasury.objects.request.account import AccountRequest


class CounterPartyRequest:
    def __init__(self, name: str, account_request_list: List[AccountRequest]):
        self.name = name
        self.account_request_list = account_request_list

    def to_json(self) -> dict:
        account_list = [account.to_json() for account in self.account_request_list]

        counter_party_json = {
            "name": self.name,
            # "accounts": account_list
        }
        return counter_party_json
