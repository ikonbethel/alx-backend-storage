#!/usr/bin/env python3
'''Task 9: Insert a document in python'''


def insert_school(mongo_collection, **kwargs):
    '''
    Inserts a new document in a collection based on kwargs.
    mongo_collection will be the pymongo collection object
    Returns the new _id.
    '''
    new_id = mongo_collection.insert_one(kwargs)
    return new_id
