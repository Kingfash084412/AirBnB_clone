#!/usr/bin/python3
""" The json file storage """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage():
    """ Create a file storage
    - serialize to JSON file and deserialize
    JSON file to instances

    Args:
        class attributtes:
            __file_path: string json ti file (file.json)
            __objects: empty dictionary
        class methods:
            all: All in the dictionary
            new: Create a new key
            save: serializes __objects to JSON path
            reload: deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel,
                  "User": User,
                  "State": State,
                  "City": City,
                  "Place": Place,
                  "Amenity": Amenity,
                  "Review": Review}

    def all(self):
        """ return the dictionary objects """
        return (self.__objects)

    def new(self, obj):
        """ set in __objects the obj with key id """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ Serialize __objects to the JSON file
        path: __file_path
        """

        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects
            if the file doesn't exist: show no errors
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
