#!/usr/bin/python
"""Amenity class represents a feature or facilitys"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class represents a feature or facility that may be available in a particular location,
    inheriting from the BaseModel.

    Attributes:
        name (str): The name of the amenity.

    Methods:
        __init__: Initializes a new Amenity instance, calling the constructor of the base class (BaseModel).
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        __init__: Initializes a new Amenity instance, calling the constructor of the base class (BaseModel).
        """
        super().__init__(*args, **kwargs)
