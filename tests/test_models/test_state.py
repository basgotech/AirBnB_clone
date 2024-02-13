#!/usr/bin/python3
"""
Contains the Test case State
"""

from datetime import datetime
import inspect
from models import state
from models.base_model import BaseModel
import pep8
import unittest

"""Alias for better readability"""
State_cl_holder = state.State


class Test_State_Mod_Documentation(unittest.TestCase):
    """
    Test suite for validating documentation in the State module.
    """

    @classmethod
    def ini_test_class_case(cls):
        """
        Initialize the test class.
        """
        cls.state_f = inspect.getmembers(State_cl_holder, inspect.isfunction)

    def test_code_style_state(self):
        """
        Validate code style for the State module.
        """
        code_style = pep8.StyleGuide(quiet=True)
        result_grapper = code_style.check_files(['models/state.py'])
        self.assertEqual(result_grapper.total_errors, 0,
                         "Found code style errors.")

    def test_code_style_test_state(self):
        """
        Validate code style for the test_state.py file.
        """
        code_style = pep8.StyleGuide(quiet=True)
        result_grapper = code_style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result_grapper.total_errors, 0,
                         "Found code style errors.")

    def test_state_bundle(self):
        """
        Check if the State module has a docstring.
        """
        self.assertIsNot(state.__doc__, None,
                         "has no docstring")
        self.assertTrue(len(state.__doc__) >= 1,
                        "has no docstring")

    def test_state_cls_doc_verify(self):
        """
        Check if the State class has a docstring.
        """
        self.assertIsNot(State_cl_holder.__doc__, None,
                         "State class has no docstring")
        self.assertTrue(len(State_cl_holder.__doc__) >= 1,
                        "State class has no docstring")

    def test_state_fun_documen_ver(self):
        """
        Validate documentation for methods in the State class.
        """
        for f_grapper in self.state_f:
            self.assertIsNot(f_grapper[1].__doc__, None,
                             "{:s} method needs a docstring".format(f_grapper[0]))
            self.assertTrue(len(f_grapper[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(f_grapper[0]))


class Test_State_class_docu(unittest.TestCase):
    """
    Test suite for functionality and documentation in the State class.
    """

    def test_state_is_subclass(self):
        """
        Validate if State is a subclass of BaseModel.
        """
        state_grapper = State_cl_holder()
        self.assertIsInstance(state_grapper, BaseModel)
        self.assertTrue(hasattr(state_grapper, "id"))
        self.assertTrue(hasattr(state_grapper, "created_at"))
        self.assertTrue(hasattr(state_grapper, "updated_at"))

    def test_state_name_entity(self):
        """
        Validate the existence and default value of 'name' attribute in State class.
        """
        state_grapper = State_cl_holder()
        self.assertTrue(hasattr(state_grapper, "name"))
        self.assertEqual(state_grapper.name, "")

    def test_to_dict_state_cr_dict(self):
        """
        Validate the creation of a dictionary representation of a State instance.
        """
        state_grapper = State_cl_holder()
        new_dictionery_state = state_grapper.to_dict()
        self.assertEqual(type(new_dictionery_state), dict)
        for has_entity in state_grapper.__dict__:
            self.assertTrue(has_entity in new_dictionery_state)
            self.assertTrue("__class__" in new_dictionery_state)

    def test_to_dict_has_val_attr(self):
        """
        Validate the values of attributes in the dictionary representation of a State instance.
        """
        timer_and_date_holder = "%Y-%m-%dT%H:%M:%S.%f"
        state_grapper = State_cl_holder()
        new_dictionery_state = state_grapper.to_dict()
        self.assertEqual(new_dictionery_state["__class__"], "State")
        self.assertEqual(type(new_dictionery_state["created_at"]), str)
        self.assertEqual(type(new_dictionery_state["updated_at"]), str)
        self.assertEqual(new_dictionery_state["created_at"], state_grapper.created_at.strftime(timer_and_date_holder))
        self.assertEqual(new_dictionery_state["updated_at"], state_grapper.updated_at.strftime(timer_and_date_holder))

    def test_state_str_testify(self):
        """
        Validate the string representation of a State instance.
        """
        state_grapper = State_cl_holder()
        str_coll = "[State] ({}) {}".format(state_grapper.id, state_grapper.__dict__)
        self.assertEqual(str_coll, str(state_grapper))
