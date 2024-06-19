#!/usr/bin/env python3
"""
10. Change school topics
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    a function that updates many rows
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
