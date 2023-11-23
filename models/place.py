#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay
     Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: description of the place
        number_rooms: number of romm
        number_bathrooms: number of bathrooms
        max_guest: maximum guest
        price_by_night: price by night
        latitude: latitude
        longitude: longitude
    """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref='place')
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates='place_amenities')

    else:
        @property
        def reviews(self):
            """ Returns list of reviews.id """
            objs = models.storage.all()
            a_list = []
            res = []
            for key in objs:
                rev = key.replace('.', ' ')
                rev = shlex.split(review)
                if (rev[0] == 'Review'):
                    a_list.append(objs[key])
            for rev in a_list:
                if (rev.place_id == self.id):
                    res.append(rev)
            return (res)

        @property
        def amenities(self):
            """ Returns list of amenity ids """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """ Appends amenity ids to the attribute """
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
