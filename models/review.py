#!/usr/bin/python3
""" a class Review that inherits from BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class for the HBNB """
    place_id = ""
    user_id = ""
    text = ""
