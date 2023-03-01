import pymongo
import API.config as cf
import certifi


ca = certifi.where()


class Database():

    def __init__(self) -> None:
        client = pymongo.MongoClient(
            f"mongodb+srv://{cf.mongodb['login']}:{cf.mongodb['password']}@cryptocluster0.azkufll.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
        self.db = client.CryptoData

    def get_collections(self):
        for collection in self.db.list_collection_names():
            print(collection)

    def get_one_coin(self, objects_ids):
        collection = self.db.coins.find({"id": objects_ids})
        return list(collection)
    
    def get_all_coins(self):
        collection = self.db.coins.find()
        return list(collection)
    
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
    db.get_collections()
    get_one_coin()
    get_all_coins()
    # update_object()
    # add_object()
    # delete_object()


# create a function to read the informations of a list of objects.

# create a function to read the informations of an object.

# create a function to modify the informations of an object.
# create a function to add a new object.
# create a function to delete an object.
