class RoutingDetailsRequest:
    def __init__(self, routing_number_type:str, routing_number:str, idempotency_key: str = None):
        self.routing_number_type = routing_number_type
        self.routing_number = routing_number
        self.idempotency_key = f"routing_details_{idempotency_key}" if idempotency_key else None

    def to_json(self):
        return {
            "routing_number_type": self.routing_number_type,
            "routing_number": self.routing_number,
        }
