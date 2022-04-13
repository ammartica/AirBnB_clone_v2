#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from models.place import Place
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from sql.alchemy.orm.exc import NoResultFound
import os


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    __classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                }

    def __init__(self):
        """ Initializes the database """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)
        if (os.getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all objects based on class provided"""
        obj_dict = {}
        if cls is None:
            for key, value in self.__classes.items():
                try:
                    result = self.__session.query(value).all()
                except NoResultFound():
                    pass
                for obj in result:
                    new_key = key + "." + obj.id
                    obj_dict[new_key] = obj
        else:
            result = self.__session.query(cls).all()
            for obj in result:
                new_key = key + "." + obj.id
                obj_dict[new_key] = obj

        return obj_dict

    def new(self, obj):
        self.__session.add(obj)
        pass

    def save(self):
        """commits the changes to the database"""
        self.__session.commit()

    def reload(self):
        ''' Creats all the tables in the current Database '''
        Base.metadata.create_all(engine)

        # Creates session factory - creates session object with given rules
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        # Session will call upon the same registry of sessions created
        # This allows us to get back the same session everytime
        Session = scoped_session(session_factory)

        # Now we have a "global" session that our app can use collectively
        self.__session = Session()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
        pass
