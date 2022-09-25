#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """
        A class for amenity object
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship('Place', secondary='place_amenity', back_populates='amenities')
