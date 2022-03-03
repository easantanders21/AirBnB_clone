#!/usr/bin/python3
""" a class User that inherits from BaseModel """

from models.base_model import BaseModel


class State(BaseModel):
    """ User class for the HBNB """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
