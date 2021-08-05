class LineItemRequest:
    def __init__(self, amount, metadata, description, accounting_category_id):
        self.amount = amount
        self.metadata = metadata
        self.description = description
        self.accounting_category_id = accounting_category_id

    def to_json(self):
        return {
            'amount': self.amount,
            'metadata': self.metadata,
            'description': self.description,
            'accounting_category_id': self.accounting_category_id
        }
