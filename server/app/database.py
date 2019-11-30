import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from gridfs import GridFS



class DB(object):

    URI = "mongodb+srv://TDSB301:csc301csc301@tdsb-x6zvw.mongodb.net/test?retryWrites=true&w=majority"


    @staticmethod
    def init():
        client = MongoClient(DB.URI)
        DB.DATABASE = client['TDSB']
        DB.FS = GridFS(DB.DATABASE)

    @staticmethod
    def insert(collection, data):
        DB.DATABASE[collection].insert(data)

    @staticmethod
    def find_one(collection, query):
        return DB.DATABASE[collection].find_one(query)

    @staticmethod
    def find(collection, query):
        return DB.DATABASE[collection].find(query)

    #need delete and update methods
    @staticmethod
    def remove(collection, query):
        DB.DATABASE[collection].remove(query)

    @staticmethod
    def update(collection, query, update, option=False):
        DB.DATABASE[collection].update(query, update, option)

    @staticmethod
    def save_file(file, filename):
        file_id = DB.FS.put(file, filename=filename)
        return file_id

    @staticmethod
    def get_file(file_id):
        return DB.FS.get(ObjectId(file_id))


    
