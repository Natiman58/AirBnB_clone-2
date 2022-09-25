#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer, FLOAT, Table
from sqlalchemy.orm import relationship

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from os import getenv

from models.review import Review

if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                          Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    __table__name = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(FLOAT, nullable=True)
    longitude = Column(FLOAT, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship('Review', backref='place', cascade='all, delete-orphan')
        amenities = relationship('Amenity', secondary='place_amenity', backref='place', viewonly=False)
    else:
        @property
        def reviews(self):
            """A getter attribute that returns list of reviews"""
            r = [review for review in models.storage.all(Review) if review.place_id == self.id]
            return r

        @property
        def amenities(self):
            """Returns the list of Amenity instances based on amenity_ids"""
            a = [amenity for amenity in models.storage.all(Amenity) if amenity.id in self.amenity_ids]
            return a

        @amenities.setter
        def amenities(self, obj):
            """Setter method handles append method
                to the attribute amenity_ids[]
            """
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
