#!/usr/bin/python3
"""
    This module instantiates an object of class FileStorage
    creates a switch to allow change of storage
    depending on the environment variable
"""
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from os import getenv

storage = FileStorage()
storage.reload()

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine import db_storage
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()

