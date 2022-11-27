#!usr/bin/python3
""" My file storage module """
import json
import os
from pathlib import Path

BASE_DIR = Path(os.getcwd()).resolve()


class FileStorage:
    """ The file storage class """
    __file_path = str(BASE_DIR / "file.json")
    __objects = {}

    def __init__(self):
        """Initialization method"""
        pass

    def all(self):
        """ Returns all of the objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ Sets a new object to the object dict """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        save_dict = {}
        if FileStorage.__objects:
            for key, value in FileStorage.__objects.items():
                save_dict[key] = value.to_dict()

            with open(FileStorage.__file_path, "w") as f:
                json.dump(save_dict, f)
        else:
            with open(FileStorage.__file_path, "w") as f:
                json.dump({}, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.
        """
        if Path(FileStorage.__file_path).exists():
            with open(FileStorage.__file_path, "r") as r:
                try:
                    reload_dict = json.load(r)
                except:
                    reload_dict = None

                if reload_dict:
                    from models.base_model import BaseModel
                    from models.user import User
                    from models.state import State
                    from models.city import City
                    from models.place import Place
                    from models.review import Review
                    from models.amenity import Amenity
                    FileStorage.__objects = {}
                    for key, value in reload_dict.items():
                        if key.startswith("BaseModel"):
                            FileStorage.__objects[key] = BaseModel(**value)
                        if key.startswith("User"):
                            FileStorage.__objects[key] = User(**value)
                        if key.startswith("State"):
                            FileStorage.__objects[key] = State(**value)
                        if key.startswith("City"):
                            FileStorage.__objects[key] = City(**value)
                        if key.startswith("Place"):
                            FileStorage.__objects[key] = Place(**value)
                        if key.startswith("Review"):
                            FileStorage.__objects[key] = Review(**value)
                        if key.startswith("Amenity"):
                            FileStorage.__objects[key] = Amenity(**value)
