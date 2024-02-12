#!/usr/bin/python
"""class represents a city entity"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class represents a city entity, inheriting from the BaseModel.

    Attributes:
        state_id (str): The identifier of the state to which the city belongs.
        name (str): The name of the city.

    Methods:
        __init__: Initializes a new City instance, calling the constructor of the base class (BaseModel).
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        __init__: Initializes a new City instance, calling the constructor of the base class (BaseModel).
        """
        super().__init__(*args, **kwargs)
