from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from .account_details import AccountDetailsRequest
from .routing_details import RoutingDetailsRequest


@dataclass
class PaymentOrderRequest:
    type: str
    amount: Decimal
    direction: str
    originating_account_id: str
    receiving_account_id: str
    fallback_type: Optional[str] = field(default=None)
    subtype: Optional[str] = field(default=None)
    account_type: Optional[str] = field(default=None)
    party_name: Optional[str] = field(default=None)
    party_type: Optional[str] = field(default=None)
    party_address: Optional[str] = field(default=None)
    plaid_processor_token: Optional[str] = field(default=None)
    accounting_category_id: Optional[str] = field(default=None)
    accounting_ledger_class_id: Optional[str] = field(default=None)
    currency: Optional[str] = field(default=None)
    effective_date: Optional[str] = field(default=None)
    priority: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    statement_descriptor: Optional[str] = field(default=None)
    remittance_information: Optional[str] = field(default=None)
    purpose: Optional[str] = field(default=None)
    line_items: Optional[str] = field(default=None)
    metadata: Optional[dict] = field(default=None)
    charge_bearer: Optional[str] = field(default=None)
    foreign_exchange_indicator: Optional[str] = field(default=None)
    foreign_exchange_contract: Optional[str] = field(default=None)
    nsf_protected: Optional[str] = field(default=None)
    originating_party_name: Optional[str] = field(default=None)
    ultimate_originating_party_name: Optional[str] = field(default=None)
    ultimate_originating_party_identifier: Optional[str] = field(default=None)
    receiving_account: Optional[str] = field(default=None)
    idempotency_key: Optional[str] = field(default=None)
    account_details: Optional[List[AccountDetailsRequest]] = field(default_factory=list)
    routing_details: Optional[List[RoutingDetailsRequest]] = field(default_factory=list)

    def __post_init__(self):
        self.amount = int(self.amount * 100)
        self.idempotency_key = f"payment_order_{self.idempotency_key}" if self.idempotency_key else None

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
            'account_details_json': account_details_json,
            'routing_details_json': routing_details_json,
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

@dataclass
class UpdatePaymentOrderRequest:
    status: Optional[str] = field(default=None)
    metadata: Optional[dict] = field(default=None)

    def to_json(self):
        return {
            "status": self.status,
            "metadata": self.metadata
        }