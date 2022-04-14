#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.engine.file_storage import FileStorage
import os

fs = FileStorage()

if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'), nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'), nullable=False))


class Place(BaseModel, Base):
    """ class represents Place object """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False)

    else:
        @property
        def reviews(self):
            """ getter method for reviews when place_id == Place.id"""
            reviews_list = []
            reviews = fs.all(Review)
            for review in reviews.values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """ getter for amenities returns lit of Amenity instances """
            amenities_list = []
            amenities = fs.all(Amenity)
            for amenity in amenities.values():
                if amenity.place_id == self.id:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """ setter method for amenities getter """
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
