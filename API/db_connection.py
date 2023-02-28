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


if __name__ == "__main__":
    db = Database()
    db.get_collections()
