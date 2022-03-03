from dataclasses import asdict, dataclass


@dataclass
class AddressRequest:
    line1: str
    line2: str
    locality: str
    region: str
    postal_code: str
    country: str

    def to_json(self) -> dict:
        return asdict(self)