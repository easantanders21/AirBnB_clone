#!/usr/bin/python3
""" The module with the BaseModel for our AirBnB project """

import uuid
from datetime import datetime
import models


class BaseModel:
    """ The class template for creating new instances of BaseModel
    """

    def __init__(self, *args, **kwargs):
        """ This is the constructor for the class Base model
        """
        if (kwargs):
            for k, v in kwargs.items():
                if (k == "__class__"):
                    continue
                if (k == "created_at" or k == "updated_at"):
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Method for the string form of the class
        """
        return("[{}] ({}) {})".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__
            of the instance
        """

        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['updated_at'] = self.updated_at.isoformat("T", "microseconds")
        my_dict['created_at'] = self.created_at.isoformat("T", "microseconds")
        return my_dict
