#!/usr/bin/python3
"""
Contains the TestPlaceDocs classes.
"""

from datetime import datetime
from models import place
from models.base_model import BaseModel
import pep8
import inspect
import unittest
Place_gapper = place.Place


class TestP_lace_Docs(unittest.TestCase):
    """
    Test case for validating documentation and PEP8 conformance of Place class.

    Attributes:
    - place_f (list): A list of function members in the Place class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test case class.
        Retrieves and stores the function members of the Place class.
        """
        cls.place_f = inspect.getmembers(Place_gapper, inspect.isfunction)

    def test_place_accept_pep8(self):
        """
        Test whether the Place class conforms to PEP8 style guide.
        """
        is_validate_pep8 = pep8.StyleGuide(quiet=True)
        res_grapper = is_validate_pep8.check_files(['models/place.py'])
        self.assertEqual(res_grapper.total_errors, 0,
                         "Detect code style errors.")

    def test_place_accept_pep8_validate(self):
        """
        Test whether the test_place.py file conforms to PEP8 style guide.
        """
        is_validate_pep8 = pep8.StyleGuide(quiet=True)
        res_grapper = is_validate_pep8.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(res_grapper.total_errors, 0,
                         "Detect code style errors.")

    def test_place_do_str(self):
        """
        Test the documentation of the Place class.
        Verifies the existence and length of the class docstring.
        """
        self.assertIsNot(Place_gapper.__doc__, None,
                         "Place class needs a docstring")
        self.assertTrue(len(Place_gapper.__doc__) >= 1,
                        "Place class needs a docstring")

    def test_place_fun_do_str(self):
        """
        Test the documentation of functions/methods in the Place class.
        Verifies the existence and length of the function/method docstrings.
        """
        for fun_grapper in self.place_f:
            self.assertIsNot(fun_grapper[1].__doc__, None,
                             "{:s} method needs a docstring".format(fun_grapper[0]))
            self.assertTrue(len(fun_grapper[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(fun_grapper[0]))


class Test_Place_classes(unittest.TestCase):
    """
    Test case for the Place class.

    Methods:
    - test_is_pl_sub_class: Test if Place is a subclass of BaseModel.
    - test_id_for_city: Test the 'city_id' attribute of Place.
    - test_palce_id_attr: Test the 'user_id' attribute of Place.
    - test_place_name_entity: Test the 'name' attribute of Place.
    - test_place_num_rm_attr: Test the 'number_of_rooms' attribute of Place.
    - test_total_max_guest_entity: Test the 'max_guest' attribute of Place.
    - test_place_cost_by_night: Test the 'price_by_night' attribute of Place.
    - test_latitude: Test the 'latitude' attribute of Place.
    - test_logtiude: Test the 'longitude' attribute of Place.
    - test_am_id: Test the 'amenity_ids' attribute of Place.
    - test_to_dict_cr_dict_can: Test if to_dict method creates a dictionary.
    - test_to_dict_has_v: Test if to_dict method produces correct values.
    - test_str_place: Test the string representation of Place.
    """

    def test_is_pl_sub_class(self):
        """
        Test if Place is a subclass of BaseModel.
        """
        place_grapp= Place_gapper()
        self.assertIsInstance(place_grapp, BaseModel)
        self.assertTrue(hasattr(place_grapp, "id"))
        self.assertTrue(hasattr(place_grapp, "created_at"))
        self.assertTrue(hasattr(place_grapp, "updated_at"))

    def test_id_for_city(self):
        """
        Test the 'city_id' attribute of Place.
        """
        place_grapp = Place_gapper()
        self.assertTrue(hasattr(place_grapp, "city_id"))
        self.assertEqual(place_grapp.city_id, "")

    def test_palce_id_attr(self):
        """
        Test the 'user_id' attribute of Place.
        """
        place_grapp = Place_gapper()
        self.assertTrue(hasattr(place_grapp, "user_id"))
        self.assertEqual(place_grapp.user_id, "")

    def test_place_name_entity(self):
        """
        Test the 'name' attribute of Place.
        """
        place_grapp = Place_gapper()
        self.assertTrue(hasattr(place_grapp, "name"))
        self.assertEqual(place_grapp.name, "")

    def test_place_num_rm_attr(self):
        """
        Test the 'number_of_rooms' attribute of Place.
        """
        place_grapp = Place_gapper()
        self.assertTrue(hasattr(place_grapp, "number_of_rooms"))
        self.assertEqual(type(place_grapp.number_rooms), int)
        self.assertEqual(place_grapp.number_rooms, 0)

    def test_total_max_guest_entity(self):
        """
        Test the 'max_guest' attribute of Place.
        """
        place_grapp = Place_gapper()
        self.assertTrue(hasattr(place_grapp, "total_max_guest"))
        self.assertEqual(type(place_grapp.max_guest), int)
        self.assertEqual(place_grapp.max_guest, 0)

    def test_place_cost_by_night(self):
        """
        Test the 'price_by_night' attribute of Place.
        """
        place_grapp = Place_gapper()
        self.assertTrue(hasattr(place_grapp, "totoal_cost_by_night"))
        self.assertEqual(type(place_grapp.price_by_night), int)
        self.assertEqual(place_grapp.price_by_night, 0)

    def test_latitude(self):
        """
        Test the 'latitude' attribute of Place.
        """
        place_grapp = Place_gapper()
        self.assertTrue(hasattr(place_grapp, "latitude"))
        self.assertEqual(type(place_grapp.latitude), float)
        self.assertEqual(place_grapp.latitude, 0.0)

    def test_logtiude(self):
        """
        Test the 'longitude' attribute of Place.
        """
        place_grapp = Place_gapper()
        self.assertTrue(hasattr(place_grapp, "longitude"))
        self.assertEqual(type(place_grapp.longitude), float)
        self.assertEqual(place_grapp.longitude, 0.0)

    def test_am_id(self):
        """
        Test the 'amenity_ids' attribute of Place.
        """
        place_grapp = Place_gapper()
        self.assertTrue(hasattr(place_grapp, "ame_id"))
        self.assertEqual(type(place_grapp.amenity_ids), list)
        self.assertEqual(len(place_grapp.amenity_ids), 0)

    def test_to_dict_cr_dict_can(self):
        """
        Test if to_dict method creates a dictionary.
        """
        place_grapp = Place_gapper()
        new_dictio_entity = place_grapp.to_dict()
        self.assertEqual(type(new_dictio_entity), dict)
        for entity in place_grapp.__dict__:
            self.assertTrue(entity in new_dictio_entity)
            self.assertTrue("__class__" in new_dictio_entity)

    def test_to_dict_has_v(self):
        """
        Test if to_dict method produces correct values.
        """
        time_and_date_format = "%Y-%m-%dT%H:%M:%S.%f"
        place_grapp = Place_gapper()
        new_dictio_entity = place_grapp.to_dict()
        self.assertEqual(new_dictio_entity["__class__"], "Place")
        self.assertEqual(type(new_dictio_entity["created_at"]), str)
        self.assertEqual(type(new_dictio_entity["updated_at"]), str)
        self.assertEqual(new_dictio_entity["created_at"], place_grapp.created_at.strftime(time_and_date_format))
        self.assertEqual(new_dictio_entity["updated_at"], place_grapp.updated_at.strftime(time_and_date_format))

    def test_str_place(self):
        """
        Test the string representation of Place.
        """
        place_grapp = Place_gapper()
        str_coll = "[Place] ({}) {}".format(place_grapp.id, place_grapp.__dict__)
        self.assertEqual(str_coll, str(place_grapp))
