import pymongo


class Database:

    URI="mongodb://127.0.0.1:27017/pricing"
    DATABASE=pymongo.MongoClient(URI).get_database()

    # URI="mongodb://127.0.0.1:27017"
    # DATABASE = None

    # @staticmethod
    # def initialize():
    #     client = pymongo.MongoClient(Database.URI)
    #     Database.DATABASE = client["item_price"]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)
    
    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)