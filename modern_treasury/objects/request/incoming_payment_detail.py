class IncomingPaymentDetailRequest:
    def __init__(self, transfer_type:str, direction:str, amount:int, virtual_account_id:str=None, internal_account_id:str=None, idempotency_key:str = None):
        self.transfer_type = transfer_type
        self.direction = direction
        self.amount = amount
        self.internal_account_id = internal_account_id
        self.virtual_account_id = virtual_account_id
        self.idempotency_key  = f"incoming_payment_detail_{idempotency_key}" if idempotency_key else None

    def to_json(self):
        result = {
            "type": self.transfer_type,
            "direction": self.direction,
            "amount": self.amount,
        }
        if self.internal_account_id:
            result["internal_account_id"] = self.internal_account_id

        if self.virtual_account_id:
            result["virtual_account_id"] = self.virtual_account_id

        return result
