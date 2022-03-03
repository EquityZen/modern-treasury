from dataclasses import dataclass


@dataclass
class RoutingDetailsRequest:
    routing_number_type: str
    routing_number:str
    idempotency_key: Optional[str] = None

    def __post__init__(self):
        self.idempotency_key = f"routing_details_{self.idempotency_key}" if self.idempotency_key else None

    def to_json(self):
        return {
            "routing_number_type": self.routing_number_type,
            "routing_number": self.routing_number,
        }
