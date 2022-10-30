#!/usr/bin/python3
"""
    A DataBase storage engine
"""
from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.amenity import Amenity
from models.base_model import Base, BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """ The new database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
            Query on current DB session for cls
            Arg: cls is the class name to inquire
        """
        if type(cls) == str:
            objs = self.__session.query(self.classes().cls())
        else:
            objs = self.__session.query(State).all()
            objs += self.__session.query(City).all()
            objs += self.__session.query(User).all()
            objs += self.__session.query(Place).all()
            objs += self.__session.query(Amenity).all()
            objs += self.__session.query(Review).all()

        dict_t = {}
        for obj in objs:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            dict_t[key] = obj
        return dict_t

    def classes(self):
        """
            To return class obj with their references
        """
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review
                   }
        return classes

    def new(self, obj):
        """To add the obj to the current database"""
        self.__session.add(obj)

    def save(self):
        """To commit all changes of the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """To delete the obj class from current database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all the tables in the DB like sqlAlchemy"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()

    def close(self):
        """To close the scoped session we created"""
        self.__session.close()
