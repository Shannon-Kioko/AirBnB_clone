#!/usr/bin/python3
"""
This module contains the City class which inherits from BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    This class defines the City model. Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
