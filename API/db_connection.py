import pymongo
import config as cf


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


if __name__ == "__main__":
    db = Database()
    db.get_collections()
