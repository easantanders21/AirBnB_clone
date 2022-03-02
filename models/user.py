#!/usr/bin/python3
""" a class User that inherits from BaseModel """

from models.base_model import BaseModel

class User(BaseModel):
    """ User class for the HBNB """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __init__(self, *args, **kwargs):
        """Constructor de clase Supervisor"""
        BaseModel.__init__(self, *args, **kwargs)