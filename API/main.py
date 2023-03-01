from flask import Flask, render_template
from gecko import geckoAPI
from db_connection import Database
from pprint import pprint

app = Flask(__name__)
gecko = geckoAPI()
db = Database()


@app.route('/', methods=['GET'])
def go_home():
    coins = db.get_all_coins()
    return render_template("dashboard.html", coins=coins)



if __name__ == "__main__":
    # app.run(debug=True)
    
    # Refresh coins data
    def refresh_coins():
        try:
            db.drop_collection("coins")
        except Exception:
            pass
        coins = gecko.get_coins_list()
        db.add_data_coins(coins)
    refresh_coins()
    
    
    
    currencies = db.get_currencies()
    for currency in currencies:
        code = currency["CurrencyCode"]
        if code in ["CNY","EUR","PHP"]:
            data = gecko.get_coins_list(code)
            for coin in data:
                date = coin["last_updated"]
                price = coin["current_price"]
                id = coin["id"]
                db.update_coin(id,price,date)
