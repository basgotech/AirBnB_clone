#!/usr/bin/python3
"""Base class for models."""
from datetime import datetime
import uuid
import models

"""Time Grap for the models created and update exe"""
get_time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Base class for models, providing common functionality for object creation,
    saving, and conversion to a dictionary.

    Attributes:
        id (str): Unique identifier for the instance.
        created_at (datetime): Timestamp indicating object creation time.
        updated_at (datetime): Timestamp indicating the last update time.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel.

        If keyword arguments are provided, populates instance attributes accordingly.
        If no arguments are provided, generates a new id and sets created_at/updated_at.
        """
        if kwargs:
            # Populate attributes from kwargs
            for key_grapp, value_grapp in kwargs.items():
                if key_grapp != "__class__":
                    setattr(self, key_grapp, value_grapp)
            # Convert string representations to datetime objects if applicable
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], get_time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], get_time)
        else:
        # Generate new id and set timestamps for a new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' timestamp and triggers the storage to save changes.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance attributes to a dictionary for serialization.

        Returns:
            dict: Dictionary representation of the instance.
        """
        new_dec_save = self.__dict__.copy()
        if "created_at" in new_dec_save:
            new_dec_save["created_at"] = new_dec_save["created_at"].strftime(get_time)
        if "updated_at" in new_dec_save:
            new_dec_save["updated_at"] = new_dec_save["updated_at"].strftime(get_time)
        new_dec_save["__class__"] = self.__class__.__name__
        return new_dec_save
