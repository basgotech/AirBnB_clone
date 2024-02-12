#!/usr/bin/python
""" A class Hold Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    A class reperesneting a place with various attr

    Attributes:
    - city_id (str): The unique identifier for the city where the place
    is located
    - user_id (str): The unique identifier fo the user who owns the place.
    - name (str) :The name of the place.
    - decription (str): A description providing details about the place.
    - number_rooms (int): The number of rooms in the place.
    - number_bathrooms (int): The number bathrooms in the place.
    - max_guest (int): The maximum number of guests the place can accomodate.
    - price_by_night (float): The per night for staying at the place.
    - latitude (float): The latitude coordinate of the place's location.
    - longtude (float): The longitude coordinate of the place's location.
    - amentiy_ids (list): A list of unique identifiers for amenties
    available in the place.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place of attributes"""
        super().__init__(*args, **kwargs)
