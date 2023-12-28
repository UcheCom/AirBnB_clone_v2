#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """Retrieves a list of all related city instances
            with state_id = to the current state id
            """
            cities_lst = []

            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    cities_lst.append(city)
            return cities_lst
