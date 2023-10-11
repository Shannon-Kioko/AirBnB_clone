"""
This module contains class BaseModel that defines all common attributes/methods for other classes
"""

import uuid
import datetime


class BaseModel:
    """
    This class defines common attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args: Unused arguments.
            **kwargs: A dictionary containing attribute name-value pairs.

        If kwargs is not empty, it initializes attributes from kwargs. 'created_at' and 'updated_at' values are
        converted from string format to datetime objects. 'id' is set to a new uuid4 string.
        If kwargs is empty, it creates 'id' and 'created_at' as in a new instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(
                        self,
                        key,
                        datetime.datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"
                        ),
                    )
                else:
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

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
                  'created_at' and 'updated_at' are converted to ISO format.
        """
        instance_dict = dict(self.__dict__)
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict
