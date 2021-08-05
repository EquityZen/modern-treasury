import json

# CONSTANTS
ACH_PAYMENT_ORDER_TYPE = "ach"
WIRE_PAYMENT_ORDER_TYPE = "wire"

class PaymentOrderResponse:
    def __init__(self, json: dict):
        self.json = json

    @property
    def id(self):
        return self.json.get('id')

    @property
    def name(self):
        return self.json.get('name')

    @property
    def amount(self):
        return self.json.get('amount')


def create_payment_order(from_account_id: str, to_account: str, amount: float, order_type: str):
    ach_json = {
        "type": order_type,
        "amount": amount,
        "direction": "credit",
        "currency": "USD",
        "originating_account_id": from_account_id,
        "receiving_account_id": to_account_id,
    }

    return json.dumps(ach_json)
