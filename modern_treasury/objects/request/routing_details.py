class RoutingDetailsRequest:
    def __init__(self, routing_number_type:str, routing_number:str):
        self.routing_number_type = routing_number_type
        self.routing_number = routing_number

    def to_json(self):
        return {
            "routing_number_type": self.routing_number_type,
            "routing_number": self.routing_number,
        }
