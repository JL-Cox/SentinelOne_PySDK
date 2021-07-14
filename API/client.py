import requests
from config import Config


class Client:

    def __init__(self, api_token=Config.api_key, limit=10, count_only=False) -> None:
        self.api_token = api_token
        self.base_url = "https://usea1-swprd1.sentinelone.net/web/api/v2.1"
        self.options = {
                        "accounts":"/accounts", 
                        "agents":"/agents"
                        }
        self.api_key = api_token
        self.auth_header={'Authorization': f"ApiToken {self.api_key}"}
        self.limit = limit
        self.count_only = count_only

    def create_account(self):
        pass

    def api_test(self):

        response = requests.get(self.base_url + self.options["agents"], headers=self.auth_header)
        
        if response.status_code == 200:
            return "Connection to the API was successfull"
        else:
            return f"Connection to the API has failed with code: {response.status_code}"
    