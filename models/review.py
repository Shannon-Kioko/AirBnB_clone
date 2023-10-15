#!/usr/bin/python3
"""
This module contains the Review class which inherits from BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class defines the Review model. Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
