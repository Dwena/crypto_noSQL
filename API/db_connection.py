import pandas as pd
import pymongo
import config as cf
import certifi
from pprint import pprint

ca = certifi.where()


class Database():

    def __init__(self) -> None:
        client = pymongo.MongoClient(
            f"mongodb+srv://{cf.mongodb['login']}:{cf.mongodb['password']}@cryptocluster0.azkufll.mongodb.net/?retryWrites=true&w=majority",
            tlsCAFile=ca)
        self.db = client.CryptoData

    def get_collections(self):
        for collection in self.db.list_collection_names():
            print(collection)

    def drop_collection(self, collection):
        self.db.drop_collection(collection)

    def add_data_coins(self, data):
        self.db.coins.insert_many(data)

    def add_data_currency(self, data):
        # for currency in data:
        #     print(currency)
        self.db.currency.insert_many(data)

    def drop_currency(self, currency):
        self.db.drop_currency(currency)

    def get_one_coin(self, objects_ids):
        collection = self.db.coins.find({"id": objects_ids})
        return list(collection)

    def get_all_coins(self):
        collection = self.db.coins.find()
        return list(collection)

    def get_currencies(self):
        return list(self.db.currency.find())

    def update_coins(self, id, price, date):
        coin = list(self.db.coins.find({"id": id}))[0]
        price_per_day = [{coin["last_updated"]: coin["current_price"]},
                         {date: price}]
        self.db.coins.update_one({"id": id},
                                 {"$set": {"current_price": price,
                                           "last_updated": date,
                                           "price_per_day": price_per_day}}
                                 )
    def get_history(self,id):
        collection = self.db.history.find({"id": id})
        return list(collection)

    def add_data_collection(self, data, collection):
        print(data)
        self.db[collection].insert_many(data)
    
    def update_specific_coin(self,id,currency,price,date):
        self.db[f'{id}_{currency}'].insert_one({"date":date,
                                                "price":price})

    def get_history_currency(self, id_coin, currency):
        collection = self.db[id_coin + '_' + currency].find()
        return collection

    # def update_object(self, collection_name, filters, updates):
    #     collection = self.db[collection_name]
    #     result = collection.update_many(filters, updates)
    #     return result.modified_count

    # def add_object(self, collection_name, data):
    #     collection = self.db[collection_name]
    #     result = collection.insert_one(data)
    #     return result.inserted_id

    # def delete_object(self, collection_name, filters):
    #     collection = self.db[collection_name]
    #     result = collection.delete_many(filters)
    #     return result.deleted_count


if __name__ == "__main__":
    db = Database()
    # db.get_collections()
    # get_one_coin()
    # get_all_coins()
    # update_object()
    # add_object()
    # delete_object()

# create a function to read the informations of a list of objects.

# create a function to read the informations of an object.

# create a function to modify the informations of an object.
# create a function to add a new object.
# create a function to delete an object.

#df_currency = pd.read_csv("currencies.csv")
#currencies = df_currency.to_dict(orient="records")
# db.add_data_currency(currencies)
# print(currencies)
