"""
This module contains class BaseModel that defines all common attributes/methods for other classes
"""

import uuid
import datetime


class BaseModel:
    """
    This class defines common attributes and methods for other classes.
    """

    def __init__(self):
        """
        Initializes a new BaseModel instance.

        Attributes:
            id (str): A unique identifier generated using uuid.uuid4().
            created_at (datetime): The datetime when the instance is created.
            updated_at (datetime): The datetime when the instance is created and updated.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the instance.
        The format is: "[<class name>] (<self.id>) <self.__dict__>"
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: A dictionary containing all attributes of the instance.
                  The '__class__' key is added with the class name.
                  'created_at' and 'updated_at' are converted to ISO format.
        """
        instance_dict = dict(self.__dict__)
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict
