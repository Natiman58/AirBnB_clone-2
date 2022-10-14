#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

import models

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiate a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs.keys():
                setattr(self, "id", str(uuid.uuid4()))
            if "created_at" not in kwargs.keys():
                setattr(self, "created_at", datetime.now())
            if "updated_at" not in kwargs.keys():
                setattr(self, "updated_at", datetime.now())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dict_t = self.__dict__.copy()
        dict_t["__class__"] = type(self).__name__
        dict_t["created_at"] = dict_t["created_at"].isoformat()
        dict_t["updated_at"] = dict_t["updated_at"].isoformat()

        if "_sa_instance_state" in dict_t.keys():
            dict_t.pop('_sa_instance_state', None)
        return dict_t

    def delete(self):
        """ TO delete the current instance from
            the storage "models.storage"
        """
        models.storage.delete(self)
