#!/usr/bin/python
"""User class, derive from Basemodel."""
from models.base_model import BaseModel

class User(BaseModel):
    """
    User class reperesents a user
    entity with attributes such as
    listed below,

    Attributes:
       email (str): The email address associated with the user.
       password (str): The password for the user's account.
       first_name (str): The first name of the use.
       last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes all user attributes"""
        super().__init__(*args, **kwargs)
