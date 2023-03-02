from flask import Flask, render_template, redirect
from time import sleep

from utils import Utils
from gecko import geckoAPI
from datetime import datetime
from db_connection import Database
from pprint import pprint

app = Flask(__name__)
gecko = geckoAPI()
db = Database()
util = Utils()


def refresh_coins():
    try:
        db.drop_collection("coins")
    except Exception:
        pass
    coins = gecko.get_coins_list()
    db.add_data_coins(coins)


@app.route('/', methods=['GET'])
def go_home():
    coins = db.get_all_coins()
    return render_template("dashboard.html", coins=coins)


@app.route('/fill', methods=['GET'])
def fill():
    num = 0
    coins = db.get_all_coins()
    for coin in coins:
        id = coin["id"]
        if id not in ["bitcoin", "ethereum", "tether"]:
            currencies = db.get_currencies()
            for currency in currencies:
                code = currency["CurrencyCode"]
                if code in ["USD", "CNY", "EUR", "PHP"]:
                    try:
                        db.drop_collection(f'{id}_{code.lower()}')
                    except Exception:
                        pass
                    if num % 10 == 0:
                        sleep(60)
                    history = gecko.get_history(id, code.lower())["prices"]

                    db.add_data_collection(history, f'{id}_{code.lower()}')

                    num += 1


@app.route('/update', methods=['GET'])
def update():
    refresh_coins()
    currencies = db.get_currencies()
    for currency in currencies:
        code = str(currency["CurrencyCode"]).lower()
        if code in ["usd", "cny", "eur", "php"]:
            data = gecko.get_coins_list(code)
            for coin in data:
                date = Utils.from_iso_to_timestamp(coin["last_updated"])
                price = coin["current_price"]
                id = coin["id"]
                if id in ["bitcoin", "ethereum", "tether",]:
                    db.update_specific_coin(id, code, price, date)
    return redirect("/")


# @app.route('/collection', methods=['GET'])
# def get_history():
#   try:
#      db.drop_collection("bitcoin_usd")
# except Exception:
#    pass
# history = gecko.get_history('bitcoin', 'usd')
# print(history)
# db.add_data_collection(history, "bitcoin_usd")
# return 'bitcoin_usd added'
# timestamp = 1669852800000 //1000  # Unix timestamp in seconds
# date = datetime.fromtimestamp(timestamp)  # create a datetime object from the timestamp
# return date.strftime('%Y-%m-%d')  # format the datetime according to your needs

@app.route('/show/<id>', methods=['GET'])
def go_popup(id):
    coins = db.get_all_coins()
    coin = db.get_one_coin(id)
    usd = Utils.get_time_from_timestamp(db.get_history_currency(id, "usd"))
    php = Utils.get_time_from_timestamp(db.get_history_currency(id, "php"))
    eur = Utils.get_time_from_timestamp(db.get_history_currency(id, "eur"))
    cny = Utils.get_time_from_timestamp(db.get_history_currency(id, "cny"))
    print(usd)
    return render_template("dashboard.html", coins=coins, coin=coin, usd=usd, php=php, eur=eur, cny=cny)


if __name__ == "__main__":
    app.run(debug=True)
    
    # def get_history():
    #     btc = []
    #     history = gecko.get_history('tether', 'usd')["prices"]
    #
    #     for(i, j) in history:
    #         btc.append({"date": i, "price": j})
    #     db.add_data_collection(btc, "tether_usd")
    #     return 'ok'
    # get_history()
