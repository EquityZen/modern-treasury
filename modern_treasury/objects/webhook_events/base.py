from decimal import Decimal


class MetaData:
    def __init__(self, json_data: dict):
        self.json_data = json_data

    @property
    def payment_type(self):
        return self.json_data.get("payment_type")

    @property
    def buyer_id(self):
        buyer_id = self.json_data.get("buyer_id")
        return int(buyer_id)

    @property
    def deal_id(self):
        deal_id = self.json_data.get("deal_id", {})
        return int(deal_id)

    @property
    def transfer_type(self):
        return self.json_data.get("transfer_type")

    @property
    def money_movement_id(self):
        return self.json_data.get("money_movement_id")


class Data:
    def __init__(self, json_data):
        self.json_data = json_data

    @property
    def amount(self):
        return Decimal(self.json_data.get("amount")) / 100

    @property
    def status(self):
        return self.json_data.get("status")

    @property
    def metadata(self):
        metadata_json = MetaData(self.json_data.get("metadata", {}))
        return metadata_json

    @property
    def error_message(self):
        return self.json_data.get("error", {}).get("message", {})


class Event:
    def __init__(self, json_data: dict):
        self.json_data = json_data
