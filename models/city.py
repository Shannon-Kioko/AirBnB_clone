#!/usr/bin/python3
"""
This module contains the City class which inherits from BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    This class defines the City model with 'state_id' and 'name' attributes.
    """

    state_id = ""
    name = ""
