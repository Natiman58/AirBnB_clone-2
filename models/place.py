#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer, FLOAT
from sqlalchemy.orm import relationship

import models
from models.base_model import BaseModel
from os import getenv

from models.review import Review


class Place(BaseModel):
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
    else:
        @property
        def reviews(self):
            """A getter attribute that returns list of reviews"""
            r = [review for review in models.storage.all(Review) if review.place_id == self.id]
            return r