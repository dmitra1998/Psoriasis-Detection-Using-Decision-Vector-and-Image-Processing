import pymongo
from bson import ObjectId


class Database(object):

    URI = "mongodb://localhost:27017/"
    DATABASE = None

    # mydb = myclient["project"]
    # mycol = mydb["users"]
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['mydatabase'] #project is database name

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one({'Decision Vector': query})
        #return Database.DATABASE[collection].find_one({'_id': ObjectId(query)})

    @staticmethod
    def update(query, new_values, collection):
        return Database.DATABASE[collection].update_one(query, new_values)

    @staticmethod
    def delete( _id, collection):
        Database.DATABASE[collection].delete_one({'_id': ObjectId(_id)})
