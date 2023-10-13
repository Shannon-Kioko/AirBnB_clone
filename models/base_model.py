#!/usr/bin/python3
"""
This module contains class BaseModel that defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    This class defines the BaseModel with common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(
                self.created_at, "%Y-%m-%dT%H:%M:%S.%f"
            )
            self.updated_at = datetime.strptime(
                self.updated_at, "%Y-%m-%dT%H:%M:%S.%f"
            )
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime
        and calls the save() method of storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        instance_dict = dict(self.__dict__)
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )
