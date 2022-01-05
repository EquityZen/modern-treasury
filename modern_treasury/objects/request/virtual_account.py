from typing import List

from .account_details import AccountDetailsRequest


class VirtualAccountRequest:
    def __init__(self, name:str, internal_account_id:str, credit_ledger_account_id:str=None,
                 debit_ledger_account_id:str=None, counterparty_id:str=None,
                 account_details_list:List[AccountDetailsRequest]=None, metadata=None,
                 idempotency_key:str = None):
        self.name = name
        self.internal_account_id = internal_account_id
        self.credit_ledger_account_id = credit_ledger_account_id
        self.debit_ledger_account_id = debit_ledger_account_id
        self.counterparty_id = counterparty_id
        self.account_details_list = [] if not account_details_list else account_details_list
        self.metadata = {} if not metadata else metadata
        self.idempotency_key = f"virtual_account_{idempotency_key}" if idempotency_key else None

    def to_json(self):
        account_details = [account_details.to_json() for account_details in self.account_details_list]

        return {
            'name': self.name,
            'internal_account_id': self.internal_account_id,
            'credit_ledger_account_id': self.credit_ledger_account_id,
            'debit_ledger_account_id': self.debit_ledger_account_id,
            'counterparty_id': self.counterparty_id,
            'account_details_list': account_details,
            'metadata': self.metadata,
        }
