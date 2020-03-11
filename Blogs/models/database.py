# -*- coding: utf-8 -*-
import pymongo

class Database(object):
    
    URI ='mongodb://127.0.0.1:27017'
    DATABASE=None
    
    
    @staticmethod
    def initialize():
        client= pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']
    
    
    @staticmethod
    def insert(collection,data):
        Database.DATABASE[collection].insert(data)
        
        
        
    @staticmethod
    def find(collection,query):  # return a cursor object
        return Database.DATABASE[collection].find(query)
        
        
    @staticmethod
    def find_one(collection,query): # return only the specific query
        return Database.DATABASE[collection].find_one(query)