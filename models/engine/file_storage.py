#!/usr/bin/python3
""" Module that serializes instances to a JSON file and deserializes JSON file to instances
"""
import json

class FileStorage:
    """ a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        """
        k = obj.__class__.__name__ +'.'+ obj.id
        self.__objects[k]= obj

    def save(self):
        """  serializes __objects to the JSON file (path: __file_path)
        """
        my_dict = {}
        for k in self.__objects:
            my_dict[k] = self.__objects[k].to_dict()
        with open(self.__file_path, "w") as myFile:
            json.dump(my_dict, myFile)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)
        """
        try: 
            with open(self.__file_path) as json_file:
                content = json_file.read()
                self.__objects = json.loads(content)
        except:
            pass
