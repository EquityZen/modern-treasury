from .address import AddressRequest


class ExternalAccountRequest():
    def __init__(self,
                 counter_party_id: str,
                 account_details: List[AccountDetailsRequest] = None,
                 routing_details: List[RoutingDetailsRequest] = None,
                 account_type:str = None,
                 party_address:AddressRequest = None,
                 idempotency_key:str = None):
        self.counter_party_id = counter_party_id
        self.account_details = account_details if account_details else []
        self.routing_details = routing_details if routing_details else []
        self.account_type = account_type
        self.party_address = party_address
        self.idempotency_key  = f"external_account_{idempotency_key}" if idempotency_key else None

    def to_json(self):
        account_details_json = [account_detail.to_json() for account_detail in self.account_details]
        routing_details_json = [routing_detail.to_json() for routing_detail in self.routing_details]
        result = {
            'counter_party_id': self.counter_party_id,
            'account_details': self.account_details,
            'routing_details': self.routing_details,
        }
        if self.account_type:
            result['account_type'] = self.account_type
        if self.party_address:
            result['party_address'] = self.party_address.to_json()

        return result
