#!/usr/bin/python3
""" Module that serializes instances to a JSON file
    and deserializes JSON file to instances
"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json


class FileStorage:
    """ a class FileStorage that serializes instances to a JSON
        file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    class_dict = {"Amenity" : Amenity, "BaseModel": BaseModel, 
                  "City" : City, "Place" : Place, "Review" : Review,
                  "State" : State, "User" : User}

    def all(self):
        """ returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        """
        k = obj.__class__.__name__ + '.' + obj.id
        self.__objects[k] = obj

    def save(self):
        """  serializes __objects to the JSON file (path: __file_path)
        """
        my_dict = {}
        for k, v in self.__objects.items():
            my_dict[k] = v.to_dict()
        with open(self.__file_path, "w") as myFile:
            json.dump(my_dict, myFile)

    def reload(self):
        """ deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists)
        """
        content = {}
        try:
            with open(self.__file_path) as json_file:
                content = json.load(json_file)
                for key, value in content.items():
                    cls_name = value["__class__"]
                    obj = eval(cls_name+"(**value)")
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
