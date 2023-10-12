#!/usr/bin/python3
"""
This module contains the class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class defines the User model with email, password, first_name, and last_name attributes.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
