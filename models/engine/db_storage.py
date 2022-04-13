#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import sqlalchemy


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        pass

    def all(self, cls=None):
        """Returns all objects based on class provided"""
        pass

    def new(self, obj):
        pass

    def save(self):
        """saves"""
        pass

    def reload(self):
        pass

    def delete(self, obj=None):
        pass
