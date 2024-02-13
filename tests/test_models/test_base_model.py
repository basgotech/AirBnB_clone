#!/usr/bin/python3
"""Test BaseModel for expected behavior and documentations"""
from datetime import datetime
import inspect
import pep8 as pycodestyle
import time
import unittest
import models
from unittest import mock
BaseModel_grapper = models.base_model.BaseModel
module_bundle = models.base_model.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """
    Test case for validating documentation and PEP8 conformance of BaseModel.

    Attributes:
    - base_funcs (list): A list of function members in the BaseModel class.
    """

    @classmethod
    def setUpClass(self):
        """
        Set up the test case class.
        Retrieves and stores the function members of the BaseModel class.
        """
        self.base_funcs = inspect.getmembers(BaseModel_grapper, inspect.isfunction)

    def test_pep8_base_conf(self):
        """
        Test whether the BaseModel class conforms to PEP8 style guide or not.
        """
        for model_path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(model_path=model_path):
                grap_errors = pycodestyle.Checker(model_path).check_all()
                self.assertEqual(grap_errors, 0)

    def test_base_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_bundle, None,
                         "base_model.py must needs a docstring")
        self.assertTrue(len(module_bundle) > 1,
                        "base_model.py have a docstring")


class TestBaseModel(unittest.TestCase):
    """
    Test case for the BaseModel class.

    Methods:
    - test_base_instantiation: Test the instantiation of BaseModel.
    - test_base_uuid: Test the uniqueness and format of the generated UUID.
    - test_base_to_dict: Test the to_dict method of BaseModel.
    - test_base_str: Test the string representation of BaseModel.
    - test_base_save: Test the save method of BaseModel.
    """

    @mock.patch('models.storage')
    def test_base_instantiation(self, m_storage):
        """
        Test the instantiation of BaseModel.
        Verifies attribute types and whether new objects are added to storage.
        """
        setting_up = BaseModel_grapper()
        self.assertIs(type(setting_up), BaseModel_grapper)
        setting_up.name = "BasFira"
        setting_up.number = 83
        list_attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
        }
        for attribute_entity, attr_type in list_attrs_types.items():
            with self.subTest(attribute_entity=attribute_entity, attr_type=attr_type):
                self.assertIn(attribute_entity, setting_up.__dict__)
                self.assertIs(type(setting_up.__dict__[attribute_entity]), attr_type)
        self.assertTrue(m_storage.new.called)
        self.assertEqual(setting_up.name, "BasFira")
        self.assertEqual(setting_up.number, 83)

    def test_base_uuid(self):
        """
        Test the uniqueness and format of the generated UUID.
        """
        setting_upI = BaseModel_grapper()
        setting_upII = BaseModel_grapper()
        for sett in [setting_upI, setting_upII]:
            uuid = sett.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(setting_upI.id, setting_upII.id)

    def test_base_to_dict(self):
        """
        Test the to_dict method of BaseModel.
        Verifies the correctness of the produced dictionary.
        """
        the_mod_grap = BaseModel_grapper()
        the_mod_grap.name = "Holberton"
        the_mod_grap.my_number = 89
        hold_grap = the_mod_grap.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(hold_grap.keys(), expected_attrs)
        self.assertEqual(hold_grap['__class__'], 'BaseModel')
        self.assertEqual(hold_grap['name'], "BasFira")
        self.assertEqual(hold_grap['my_number'], 83)

    def test_base_str(self):
        """
        Test the string representation of BaseModel.
        """
        setting_up = BaseModel_grapper()
        string = "[BaseModel] ({}) {}".format(setting_up.id, setting_up.__dict__)
        self.assertEqual(string, str(setting_up))

    @mock.patch('models.storage')
    def test_base_save(self, m_storage):
        """
        Test the save method of BaseModel.
        Verifies the update of 'updated_at' and calls to the storage save method.
        """
        setting_up = BaseModel_grapper()
        pre_cre_at = setting_up.created_at
        pre_mod_at = setting_up.updated_at
        setting_up.save()
        let_created_at = setting_up.created_at
        let_updated_at = setting_up.updated_at
        self.assertNotEqual(pre_mod_at, let_updated_at)
        self.assertEqual(pre_cre_at, let_created_at)
        self.assertTrue(m_storage.save.called)
