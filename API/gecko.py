import config as cf
import requests
from pprint import pprint


class geckoAPI():
    def __init__(self) -> None:
        self.base_url = cf.gecko_api["url"]
        self.header = cf.gecko_api["header"]

    def get_coins_list(self):
        coins_data = []
        response = requests.get(
            f"{self.base_url}coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false",
            self.header)
        return response.json()

    def get_history(self, id, currency):
        response = requests.get(
            f"{self.base_url}coins/{id}/market_chart?vs_currency={currency}&days=91", self.header)
        return response.json()


if __name__ == "__main__":
    gecko = geckoAPI()
    pprint(gecko.get_coins_list())
