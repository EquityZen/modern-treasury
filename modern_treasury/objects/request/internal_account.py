from typing import Optional


class InternalAccountRequest():
    def __init__(self,
                 connection_id: str,
                 name: str,
                 party_name: str,
                 currency: str,
                 entity_id: Optional[str] = None,
                 idempotency_key: Optional[str] = None):
        self.connection_id = connection_id
        self.name = name
        self.party_name = party_name
        self.currency = currency
        self.entity_id = entity_id
        self.idempotency_key  = f"intenal_account_{idempotency_key}" if idempotency_key else None

    def to_json(self):
        return {
            "connection_id": self.connection_id,
            "name": self.name,
            "party_name": self.party_name,
            "currency": self.currency,
            "entity_id": self.entity_id
        }
