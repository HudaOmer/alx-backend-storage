#!/usr/bin/env python3
"""
11. Where can I learn Python?
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    a function that Finds by topic
    """
    return mongo_collection.find({"topics": topic})
