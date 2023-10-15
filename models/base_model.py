#!/usr/bin/python3
"""
This module contains class BaseModel that defines
all common attributes/methods for other classes.
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project.

    Attributes:
        id (str): A unique identifier for the instance.
        created_at (datetime): The date and time the instance was created.
        updated_at (datetime): The date and time the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime and save to storage."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Returns:
            dict: A dictionary representation of the instance,
            including __class__.
        """
        result_dict = self.__dict__.copy()
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        result_dict["__class__"] = self.__class__.__name__
        return result_dict

    def __str__(self):
        """Return the string representation of the BaseModel instance.

        Returns:
            str: A string in the format "[class name] (id) {attributes}".
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
