import config as cf
import requests
from pprint import pprint


class geckoAPI():
    def __init__(self) -> None:
        self.base_url = cf.gecko_api["url"]
        self.header = cf.gecko_api["header"]

    def get_coins_list(self,code="usd"):
        response = requests.get(
            f"{self.base_url}coins/markets?vs_currency={code}&order=market_cap_desc&per_page=250&page=1&sparkline=false",
            self.header)
        return response.json()
    # recuperer premiere 250 coins 

    def get_history(self, id, currency):
        response = requests.get(
            f"{self.base_url}coins/{id}/market_chart?vs_currency={currency}&days=91", self.header)
        print(response.json())
        return response.json()
    # on recupere les 91 derniers jours de l'historique de la crypto monnaie choisie dans la devise choisie


if __name__ == "__main__":
    gecko = geckoAPI()
    # pprint(gecko.get_coins_list())
