#!/usr/bin/python3
"""
Contains the File Storage for Base Models.
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
           "Amenity": Amenity, 
           "BaseModel": BaseModel, 
           "City": City,
           "Place": Place, 
           "Review": Review, 
           "State": State, 
           "User": User
           }


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    
    __objetcs = {}

    def all(self):
        """Returns the dictionery __objects."""
        return self.__objetcs

    def new(self, obj):
        """Sets in __objects the obj with key <obj clas name>.id"""
        if obj is not None:
            key_grapp = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objetcs[key_grapp] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key_grapp in self.__objetcs:
            serialized_objects[key_grapp] = self.__objetcs[key_grapp].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                json_file = json.load(file)
            for key_grapp in json_file:
                self.__objetcs[key_grapp] = classes[json_file[key_grapp]["__class__"]](**json_file[key_grapp])
        except:
            pass
