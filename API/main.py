from flask import Flask, render_template
from gecko import geckoAPI
from db_connection import Database

app = Flask(__name__)
# gecko = geckoAPI()
db = Database()


@app.route('/', methods=['GET'])
def go_home():
    coins = db.get_all_coins()
    return render_template("dashboard.html", coins=coins)


# @app.route("/refresh_coins", methods=['GET'])
# def refresh_coins():
#     try:
#         db.drop_collection("coins")
#     except Exception:
#         pass
#     coins = gecko.get_coins_list()
#     db.add_data_coins(coins)




if __name__ == "__main__":
     app.run()
#     try:
#         db.drop_collection("coins")
#     except Exception:
#         pass
#     coins = gecko.get_coins_list()
#     db.add_data_coins(coins)