import pymongo, os
from dotenv import load_dotenv


load_dotenv()


class Database:

    # URI="mongodb://127.0.0.1:27017/pricing"
    DATABASE=pymongo.MongoClient(os.environ.get("URI")).get_database()

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)
    
    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        return Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        return Database.DATABASE[collection].remove(query)  

