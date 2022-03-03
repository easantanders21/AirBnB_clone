#!/usr/bin/python3
""" a class City that inherits from BaseModel """

from models.base_model import BaseModel


class City(BaseModel):
    """ City class for the HBNB """
    name = ""
    state_id = ""
