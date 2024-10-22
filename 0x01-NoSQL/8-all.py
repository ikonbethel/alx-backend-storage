#!/usr/bin/env python3
'''Task 8: Lists all documents in collection'''


def list_all(mongo_collection):
    '''
    Lists all documents in a collection.
    Returns an empty list if no document in the collection.
    '''
    return [doc for doc in mongo_collection.find()]
