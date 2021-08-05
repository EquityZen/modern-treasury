class AddressRequest:
    def __init__(self, line1, line2, locality, region, postal_code, country):
        self.line1 = line1
        self.line2 = line2
        self.locality = locality
        self.region = region
        self.postal_code = postal_code
        self.country = country

    def to_json(self) -> dict:
        return {
            'line1' : self.line1,
            'line2' : self.line2,
            'locality' : self.locality,
            'region' : self.region,
            'postal_code' : self.postal_code,
            'country' : self.country,
        }
