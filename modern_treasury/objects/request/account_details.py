class AccountDetailsRequest:
    def __init__(self, account_number: str, account_number_type:str):
        self.account_number = account_number
        self.account_number_type = account_number_type

    def to_json(self):
        return {
            'account_number': self.account_number,
            'account_number_type': self.account_number_type,
        }
