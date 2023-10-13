#!/usr/bin/python3
"""
This module defines the FileStorage class to manage serialization/deserialization.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
    }

    def all(self, cls=None):
        if cls is not None:
            return {
                k: v
                for k, v in FileStorage.__objects.items()
                if isinstance(v, cls)
            }
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.______name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
            for key, value in obj_dict.items():
                cls_name, obj_id = key.split(".")
                obj = FileStorage.__objects.get(cls_name)
                if obj:
                    obj = obj(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
