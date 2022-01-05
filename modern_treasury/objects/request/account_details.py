class AccountDetailsRequest:
    def __init__(self, account_number: str, account_number_type:str, idempotency_key: str = None):
        self.account_number = account_number
        self.account_number_type = account_number_type
        self.idempotency_key = f"account_details_{idempotency_key}" if idempotency_key else None

    def to_json(self):
        return {
            'account_number': self.account_number,
            'account_number_type': self.account_number_type,
        }
