class ExpectedPaymentRequest:
    def __init__(self, amount_upper_bound: int, amount_lower_bound: int, internal_account_id: str,
                 direction: str, type: str= None, currency: str = None,
                 date_upper_bound: str = None, date_lower_bound: str = None,
                 description: str = None, statement_descriptor: str = None,
                 metadata: dict = None, counterparty_id: str = None,
                 line_items=None, idempotency_key:str = None):
        self.amount_upper_bound = amount_upper_bound
        self.amount_lower_bound = amount_lower_bound
        self.direction = direction # see DirectionTypes
        self.internal_account_id = internal_account_id
        self.type = type
        self.currency = currency
        self.date_upper_bound = date_upper_bound
        self.date_lower_bound = date_lower_bound
        self.description = description
        self.statement_descriptor = statement_descriptor
        self.metadata = {} if not metadata else {}
        self.line_items = [] if not line_items else line_items
        self.counterparty_id = counterparty_id
        self.idempotency_key = f"expected_payment_{idempotency_key}" if idempotency_key else None

    def to_json(self):
        return {
            'amount_upper_bound': self.amount_upper_bound,
            'amount_lower_bound': self.amount_upper_bound,
            'direction': self.direction,
            'internal_account_id': self.internal_account_id,
            'type': self.type,
            'currency': self.currency,
            "date_upper_bound": self.date_upper_bound,
            "date_lower_bound": self.date_lower_bound,
            "statement_descriptor": self.statement_descriptor,
            "metadata": self.metadata,
            "counterparty_id": self.counterparty_id,
            "line_items": [line_item.to_json for line_item in self.line_items],
        }
