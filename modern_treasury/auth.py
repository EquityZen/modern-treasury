import requests

class Auth:
    @classmethod
    def get_auth(cls, organization_id, api_key):
        response = requests.get('https://app.moderntreasury.com/api/ping',
                         auth=(organization_id, api_key))
        return response
