#!/usr/bin/python
"""state class reperesnts a state entry"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class reperesnets a state entity an
    attribute for the state name's

    Attributes:
      name (str): The name of the state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new state object with the
        provided name.
        """
        super().__init__(*args, **kwargs)
