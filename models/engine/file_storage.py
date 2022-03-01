#!/usr/bin/python3
""" Module that serializes instances to a JSON file and deserializes JSON file to instances
"""

class FileStorage:
    """ a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = []
    
    def all(self):
        return FileStorage.__objects