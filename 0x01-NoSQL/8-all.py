#!/usr/bin/env python3
"""
8. List all documents in Python
"""
import pymongo


def list_all(mongo_collection):
    """
    a function that lists all collections
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
