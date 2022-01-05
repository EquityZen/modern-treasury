from typing import List

from .account import AccountRequest


class CounterPartyRequest():
    def __init__(self, name: str, metadata:dict, account_request_list: List[AccountRequest], idempotency_key: str = None):
        self.name = name
        self.account_request_list = account_request_list
        self.metadata = metadata # values should be a string or None
        self.idempotency_key = f"counterparty_{idempotency_key}" if idempotency_key else None

    def to_json(self) -> dict:
        account_list = [account.to_json() for account in self.account_request_list]

        counter_party_json = {
            "name": self.name,
            "accounts": account_list,
            "metadata": self.metadata,
        }
        return counter_party_json
