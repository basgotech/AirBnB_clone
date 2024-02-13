#!/usr/bin/python3
"""
Contains the Test City.
"""

from datetime import datetime
import inspect
from models import city
from models.base_model import BaseModel
import pep8
import unittest

"""Initilize city class"""
City_grapper = city.City


class Test_city_doc_style(unittest.TestCase):
    """
    Test case for validating documentation and PEP8 conformance of City class.

    Attributes:
    - city_f (list): A list of function members in the City class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test case class.
        Retrieves and stores the function members of the City class.
        """
        cls.city_f = inspect.getmembers(City_grapper, inspect.isfunction)

    def test_pep8_agreement_city(self):
        """
        Test whether the City class conforms to PEP8 style guide.
        """
        pep8_validate = pep8.StyleGuide(quiet=True)
        grapp_result = pep8_validate.check_files(['models/city.py'])
        self.assertEqual(grapp_result.total_errors, 0,
                         "Found code style bug error.")

    def test_pep8_agreement_test_city(self):
        """
        Test whether the test_city.py file conforms to PEP8 style guide.
        """
        pep8_validate = pep8.StyleGuide(quiet=True)
        grapp_result = pep8_validate.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(grapp_result.total_errors, 0,
                         "Found code style bug error.")

    def test_city_mod_doc(self):
        """
        Test the documentation of the city module.
        Verifies the existence and length of the module docstring.
        """
        self.assertIsNot(city.__doc__, None,
                         "city.py must have a docstring city")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py must have a docstring city")

    def test_city_class_doc(self):
        """
        Test the documentation of the City class.
        Verifies the existence and length of the class docstring.
        """
        self.assertIsNot(City_grapper.__doc__, None,
                         "City class must have a docstring city")
        self.assertTrue(len(City_grapper.__doc__) >= 1,
                        "City class must have a docstring city")


class TestCity(unittest.TestCase):
    """
    Test case for the City class.

    Methods:
    - test_subclass_city: Test if City is a subclass of BaseModel.
    - test_city_name_entity_att: Test the 'name' attribute of City.
    - test_state_id_entity_attr: Test the 'state_id' attribute of City.
    - test_to_dict_cre_city_dic: Test if to_dict method creates a dictionary.
    - test_city_to_dict_data: Test if to_dict method produces correct values.
    - test_city_str_attr: Test the string representation of City.
    """

    def test_subclass_city(self):
        """
        Test if City is a subclass of BaseModel.
        """
        grapp_city = City_grapper()
        self.assertIsInstance(grapp_city, BaseModel)
        self.assertTrue(hasattr(grapp_city, "id"))
        self.assertTrue(hasattr(grapp_city, "created_at"))
        self.assertTrue(hasattr(grapp_city, "updated_at"))

    def test_city_name_entity_att(self):
        """
        Test the 'name' attribute of City.
        """
        grapp_city = City_grapper()
        self.assertTrue(hasattr(grapp_city, "name"))
        self.assertEqual(grapp_city.name, "")

    def test_state_id_entity_attr(self):
        """
        Test the 'state_id' attribute of City.
        """
        grapp_city = City_grapper()
        self.assertTrue(hasattr(grapp_city, "state_id"))
        self.assertEqual(grapp_city.state_id, "")

    def test_to_dict_cre_city_dic(self):
        """
        Test if to_dict method creates a dictionary.
        """
        grapp_city = City_grapper()
        enhance_dec = grapp_city.to_dict()
        self.assertEqual(type(enhance_dec), dict)
        for entity_grapper in grapp_city.__dict__:
            self.assertTrue(entity_grapper in enhance_dec)
            self.assertTrue("__class__" in enhance_dec)

    def test_city_to_dict_data(self):
        """
        Test if to_dict method produces correct values.
        """
        time_date_format = "%Y-%m-%dT%H:%M:%S.%f"
        grapp_city = City_grapper()
        enhance_dec = grapp_city.to_dict()
        self.assertEqual(enhance_dec["__class__"], "City")
        self.assertEqual(type(enhance_dec["created_at"]), str)
        self.assertEqual(type(enhance_dec["updated_at"]), str)
        self.assertEqual(enhance_dec["created_at"], grapp_city.created_at.strftime(time_date_format))
        self.assertEqual(enhance_dec["updated_at"], grapp_city.updated_at.strftime(time_date_format))

    def test_city_str_attr(self):
        """
        Test the string representation of City.
        """
        grapp_city = City_grapper()
        str_coll_f = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str_coll_f, str(grapp_city))
