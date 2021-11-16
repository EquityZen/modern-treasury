from typing import List

from .account_details import AccountDetailsRequest
from .routing_details import RoutingDetailsRequest


class PaymentOrderRequest:
    def __init__(self, type:str, amount:int, direction, originating_account_id=None,
                 subtype:str = None, fallback_type:str = None, receiving_account_id:str = None,
                 receiving_account:AccountDetailsRequest=None,
                 account_type:str = None, party_name:str = None,
                 party_type:str = None, party_address:str = None, account_details: List[AccountDetailsRequest] = None,
                 plaid_processor_token:str = None, routing_details: List[RoutingDetailsRequest] = None,
                 accounting_category_id:str = None, accounting_ledger_class_id:str = None,
                 currency:str = None, effective_date:str = None, priority:str = None,
                 description:str = None, statement_descriptor:str = None,
                 remittance_information:str = None, purpose:str = None, line_items:str = None,
                 metadata:dict = None, charge_bearer:str = None, foreign_exchange_indicator:str = None,
                 foreign_exchange_contract:str = None, nsf_protected:str = None,
                 originating_party_name:str = None, ultimate_originating_party_name:str = None,
                 ultimate_originating_party_identifier:str = None):

        self.type = type # One of ach, wire, check, book, rtp, etc.
        self.fallback_type = fallback_type
        self.subtype = subtype
        self.amount = amount
        self.direction = direction
        self.originating_account_id = originating_account_id
        self.receiving_account_id = receiving_account_id
        self.account_type = account_type
        self.party_name = party_name
        self.party_type = party_type
        self.party_address = party_address
        self.account_details = account_details if account_details else []
        self.plaid_processor_token = plaid_processor_token
        self.routing_details = routing_details if routing_details else []
        self.accounting_category_id = accounting_category_id
        self.accounting_ledger_class_id = accounting_ledger_class_id
        self.currency = currency
        self.effective_date = effective_date
        self.priority = priority
        self.description = description
        self.statement_descriptor = statement_descriptor
        self.remittance_information = remittance_information
        self.purpose = purpose
        self.line_items = line_items
        self.metadata = metadata
        self.charge_bearer = charge_bearer
        self.foreign_exchange_indicator = foreign_exchange_indicator
        self.foreign_exchange_contract = foreign_exchange_contract
        self.nsf_protected = nsf_protected
        self.originating_party_name = originating_party_name
        self.ultimate_originating_party_name = ultimate_originating_party_name
        self.ultimate_originating_party_identifier = ultimate_originating_party_identifier
        self.receiving_account = receiving_account

    def to_json(self):
        account_details_json = [account_detail.to_json() for account_detail in self.account_details]
        routing_details_json = [routing_detail.to_json() for routing_detail in self.routing_details]
        request = {
            'type': self.type,
            'fallback_type ': self.fallback_type,
            'subtype': self.subtype,
            'amount': self.amount,
            'direction': self.direction,
            'originating_account_id': self.originating_account_id,
            'receiving_account_id': self.receiving_account_id ,
            'account_type': self.account_type,
            # # 'party_name': self.party_name,
            # # 'party_type': self.party_type,
            # # 'party_address': self.party_address,
            # # 'account_details': account_details_json,
            # # 'plaid_processor_token': self.plaid_processor_token,
            # # 'routing_details': routing_details_json,
            # # 'accounting_category_id': self.accounting_category_id,
            # # 'accounting_ledger_class_id': self.accounting_ledger_class_id,
            # 'currency': self.currency,
            # # 'effective_date': self.effective_date,
            # # 'priority': self.priority,
            # # 'description': self.description,
            # # 'statement_descriptor': self.statement_descriptor,
            # # 'remittance_information': self.remittance_information,
            # # 'purpose': self.purpose,
            # # 'line_items': self.line_items,
            # # 'metadata': self.metadata,
            # # 'charge_bearer': self.charge_bearer,
            # # 'foreign_exchange_indicator': self.foreign_exchange_indicator,
            # # 'foreign_exchange_contract': self.foreign_exchange_contract,
            # # 'nsf_protected': self.nsf_protected,
            # # 'originating_party_name': self.originating_party_name,
            # # 'ultimate_originating_party_name': self.ultimate_originating_party_name,
            # # 'ultimate_originating_party_identifier': self.ultimate_originating_party_identifier,
        }
        if self.receiving_account:
            request['receiving_account'] = self.receiving_account.to_json()
        if self.metadata:
            request['metadata'] = self.metadata
        return request
