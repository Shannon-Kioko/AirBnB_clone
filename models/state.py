#!/usr/bin/python3
"""
This module contains the State class which inherits from BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    This class defines the State model. Attributes:
        name (str): The name of the state.
    """

    name = ""
