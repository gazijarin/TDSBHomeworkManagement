import pymongo
from pymongo import MongoClient



class DB(object):

    URI = "mongodb+srv://TDSB301:csc301csc301@tdsb-x6zvw.mongodb.net/test?retryWrites=true&w=majority"


    @staticmethod
    def init():
        client = MongoClient(DB.URI)
        DB.DATABASE = client['TDSB']

    @staticmethod
    def insert(collection, data):
        DB.DATABASE[collection].insert(data)

    @staticmethod
    def find_one(collection, query):
        return DB.DATABASE[collection].find_one(query)

    #need delete and update methods
