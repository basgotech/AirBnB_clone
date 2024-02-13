#!/usr/bin/python3
"""
Define unittest test case for model amenity.
"""

from datetime import datetime
import inspect
import pep8
import unittest
from models import amenity
from models.base_model import BaseModel
Amenity = amenity.Amenity


class TestAmenityProveDoc(unittest.TestCase):
    """
    Test case for validating and testing the code style of Amentiy class using pep8.

    Attributes:
    - amenity_f (list): A list of function members in the Amentiy class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Configure the test case class as constractor.
        Retrives and stores the function members of the Amentiy class.
        """
        cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_confi_amenity(self):
        """
        Test if the Amentiy class confirms to PEP8 style lead.
        """
        conf_pep8 = pep8.StyleGuide(quiet=True)
        grap_result = conf_pep8.check_files(['models/amenity.py'])
        self.assertEqual(grap_result.total_errors, 0,
                         "Found code style bug error.")


class TestAmenity(unittest.TestCase):
    """
    Test case for the Amentiy class.

    Methods:
    - test_is_subclass_basemodel: Test if Amentiy is a subclass of basemodel.
    - test_amenty_name_attr: Test if Amenty has the attribute 'name'.
    - test_amenty_to_dict_cr_dict: Test if to_dict method creates a dictionery.
    - test_amenty_to_dict_values: test if to_dict method produces correct values.
    - test_amenty_str: Test the string reperesentation of Amenty.
    """
    def test_is_subclass_basemodel(self):
        """
        Test if Amentiy is a subclass of BaseModel.
        """
        amenity_tester = Amenity()
        self.assertIsInstance(amenity_tester, BaseModel)
        self.assertTrue(hasattr(amenity_tester, "id"))
        self.assertTrue(hasattr(amenity_tester, "created_at"))
        self.assertTrue(hasattr(amenity_tester, "updated_at"))

    def test_amenty_name_attr(self):
        """
        Test if Amentiy has the attribute 'name'.
        """
        amenity_tester = Amenity()
        self.assertTrue(hasattr(amenity_tester, "name"))
        self.assertEqual(amenity_tester.name, "")

    def test_amenty_to_dict_cr_dict(self):
        """
        Test if to_dict method creates a dictionery.
        """
        amenity_tester = Amenity()
        new_dictionery_grap = amenity_tester.to_dict()
        self.assertEqual(type(new_dictionery_grap), dict)
        for attr_entity in amenity_tester.__dict__:
            self.assertTrue(attr_entity in new_dictionery_grap)
            self.assertTrue("__class__" in new_dictionery_grap)

    def test_amenty_to_dict_values(self):
        """
        Test if to_dict method produces correct values.
        """
        time_and_date_frmt = "%Y-%m-%dT%H:%M:%S.%f"
        amenity_tester = Amenity()
        new_dictionery_grap = amenity_tester.to_dict()
        self.assertEqual(new_dictionery_grap["__class__"], "Amenity")
        self.assertEqual(type(new_dictionery_grap["created_at"]), str)
        self.assertEqual(type(new_dictionery_grap["updated_at"]), str)
        self.assertEqual(new_dictionery_grap["created_at"], amenity_tester.created_at.strftime(time_and_date_frmt))
        self.assertEqual(new_dictionery_grap["updated_at"], amenity_tester.updated_at.strftime(time_and_date_frmt))

    def test_amenty_str(self):
        """
        test the string reperesentation of Amenty.
        """
        amenity_tester = Amenity()
        string = "[Amenity] ({}) {}".format(amenity_tester.id, amenity_tester.__dict__)
        self.assertEqual(string, str(amenity_tester))
