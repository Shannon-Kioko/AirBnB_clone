#!/usr/bin/python3
"""
This module defines the FileStorage class.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects.

        Returns:
            dict: A dictionary containing all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id

        Args:
            obj (BaseModel): The object to be stored.
        """
        object_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(object_class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        current_objects = FileStorage.__objects
        serialized_objects = {obj: current_objects[obj].to_dict() for obj in current_objects.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                deserialized_objects = json.load(file)
                for object_data in deserialized_objects.values():
                    class_name = object_data["__class__"]
                    del object_data["__class__"]
                    self.new(eval(class_name)(**object_data))
        except FileNotFoundError:
            return
