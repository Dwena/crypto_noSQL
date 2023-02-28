import pymongo
import config as cf

class DBConnection():
    def __init__(self) -> None:
        client = pymongo.MongoClient(f"mongodb+srv://{cf.mongodb['login']}:{cf.mongodb['password']}@cryptocluster0.azkufll.mongodb.net/?retryWrites=true&w=majority")
        self.db = client.CryptoData