#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey
from models.city import City
import os
from models.engine.file_storage import FileStorage

fs = FileStorage()


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
        cities = relationship("City", backref="state",
                              cascade='all, delete, delete-orphan')
    else:
        @property
        def reviews(self):
            """ getter method for reviews when place_id == Place.id"""
            cities_list = []
            cities = fs.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
