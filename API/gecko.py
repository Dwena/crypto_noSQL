import config as cf
import requests

class geckoAPI():
    def __init__(self) -> None:
        self.base_url=cf.gecko_api["url"]
        self.header=cf.gecko_api["header"]
    
    def get_coins_list(self):
        requests.get(self.base_url)