#!/usr/bin/python
""" A Class Reperesenting a review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A Calass Reperesenting a review with essential
    attributes.

    Attributes:
    - place_id (str): The unique identifier for the place associated
    with the review.
    - user_id (str): The unique identifier for the user who wrote
    the review
    - txt (str): The text content of the review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review with place_id , user_id and text attr"""
        super().__init__(*args, **kwargs)
