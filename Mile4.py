#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self,USER,PASS):
        # Intitalizing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto enviroment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'ChangeMe23'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30031
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
# Complete this create method to implement the C in CRUD
    def create(self,data):
        if data is not None:
            self.database.animals.insert_one(data) # data should be dictionary
            return True 
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False
            
# Create method to implement the R in CRUD.
    def read(self,criteria):
        if criteria is not None:
            if criteria:
                data = self.database.animals.find(criteria)
                return data
        else:
            exception = "Nothing to search, because search data is empty"
            return exception
    def readAll(self,criteria):
        data = self.database.animals.find(criteria)
        return data
        
# Method to implement the U in CRUD
    def update(self, searchData, updateData):
        if searchData is not None:
            result = self.database.animals.update_many(searchData, {"$set" : updateData})
            return result.raw_result
        else:
            return "{}"
        
        return result.raw_result
    
# Method to implement the D in CRUD
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return "{}"
        
        return result.raw_result