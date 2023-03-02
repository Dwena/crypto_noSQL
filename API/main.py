from flask import Flask, render_template
from gecko import geckoAPI
from datetime import datetime
from db_connection import Database

app = Flask(__name__)
gecko = geckoAPI()
db = Database()


@app.route('/', methods=['GET'])
def go_home():
    coins = db.get_all_coins()
    return render_template("dashboard.html", coins=coins)


#@app.route('/collection', methods=['GET'])
#def get_history():
 #   try:
  #      db.drop_collection("bitcoin_usd")
   # except Exception:
    #    pass
    #history = gecko.get_history('bitcoin', 'usd')
    #print(history)
    #db.add_data_collection(history, "bitcoin_usd")
    #return 'bitcoin_usd added'
    # timestamp = 1669852800000 //1000  # Unix timestamp in seconds
    # date = datetime.fromtimestamp(timestamp)  # create a datetime object from the timestamp
    # return date.strftime('%Y-%m-%d')  # format the datetime according to your needs

@app.route('/show/<id>', methods=['GET'])
def go_popup(id):
    coins = db.get_all_coins()
    coin = db.get_one_coin(id)
    return render_template("dashboard.html", coins=coins, coin=coin)


# @app.route("/refresh_coins", methods=['GET'])
# def refresh_coins():
#     try:
#         db.drop_collection("coins")
#     except Exception:
#         pass
#     coins = gecko.get_coins_list()
#     db.add_data_coins(coins)

if __name__ == "__main__":
    # def get_history():
    #     btc = []
    #     history = gecko.get_history('tether', 'usd')["prices"]
    #
    #     for(i, j) in history:
    #         btc.append({"date": i, "price": j})
    #     db.add_data_collection(btc, "tether_usd")
    #     return 'ok'
    # get_history()
    # app.run()
    # try:
    #     db.drop_collection("coins")
    # except Exception:
    #     pass
    # coins = gecko.get_coins_list()
    # db.add_data_coins(coins)
    app.run()