from flask import Flask, render_template
from gecko import geckoAPI
from db_connection import Database
from pprint import pprint

app = Flask(__name__)
gecko = geckoAPI()
db = Database()


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


@app.route('/update', methods=['GET'])
def update():
    refresh_coins()
    currencies = db.get_currencies()
    for currency in currencies:
        code = currency["CurrencyCode"]
        if code in ["USD", "CNY", "EUR", "PHP"]:
            data = gecko.get_coins_list(code)
            for coin in data:
                date = coin["last_updated"]
                price = coin["current_price"]
                id = coin["id"]
                if id in ["bitcoin", "ethereum", "tether"]:
                    db.update_specific_coin(id, code, price, date)


if __name__ == "__main__":
    app.run(debug=True)

    # update()
