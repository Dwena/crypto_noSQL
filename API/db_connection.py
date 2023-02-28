import pymongo
import config as cf
import pandas as pd


class Database():
    def __init__(self) -> None:
        client = pymongo.MongoClient(
            f"mongodb+srv://{cf.mongodb['login']}:{cf.mongodb['password']}@cryptocluster0.azkufll.mongodb.net/?retryWrites=true&w=majority")
        self.db = client.CryptoData
    
    def get_collections(self):
        for collection in self.db.list_collection_names():
            print(collection)
            
    def drop_collection(self,collection):
        self.db.drop_collection(collection)
            
    def add_data_coins(self,data):
        self.db.coins.insert_many(data)        

    def add_data_currency(self,data):
        # for currency in data:
        #     print(currency)
        self.db.currency.insert_many(data)

    def drop_currency(self,currency):
        self.db.drop_currency(currency)


if __name__ == "__main__":
    db = Database()
    db.get_collections()
    
    df_currency = pd.read_csv("currencies.csv")
    currencies = df_currency.to_dict(orient="records")
    db.add_data_currency(currencies)
    print(currencies)