#!/usr/bin/python3
"""Database storage"""
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import (create_engine)
import models
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """Database storage class
    Attributes: __engine, __session
    """
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Method that queries on the currect database session"""
        obj_dict = {}

        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for obj in query:
                k = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[k] = obj
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for o_cls in classes:
                query = self.__session.query(o_cls)
                for obj in query:
                    k = "{}.{}".format(type(obj).__name__, obj.id)
                    obj_dict[k] = obj
        return (obj_dict)

    def new(self, obj):
        """Method  adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Method  commits all changes of the current database session"""

        self.__session.commit()

    def delete(self, obj=None):
        """Method deletes from the current database
        session obj if not None"""

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Method creates all tables in the database"""

        Base.metadata.create_all(self.__engine)
        m_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(m_session)
        self.__session = Session()

    def close(self):
        """Method closes the session"""
        self.__session.close()
