#!/usr/bin/python3
"""
Contains the TestUserDocs classes
"""

from datetime import datetime
import inspect
from models import user
from models.base_model import BaseModel
import pep8
import unittest


User_Holder = user.User


class Test_User_modeule_Docs(unittest.TestCase):
    """
    Test suite for validating documentation in the User module.
    """

    @classmethod
    def ini_test_class_case(cls):
        """
        Initialize the test class.
        """
        cls.user_f = inspect.getmembers(User_Holder, inspect.isfunction)

    def test_code_style_verify_user(self):
        """
        Validate code style for the User module.
        """
        code_style = pep8.StyleGuide(quiet=True)
        grapp_result = code_style.check_files(['models/user.py'])
        self.assertEqual(grapp_result.total_errors, 0,
                         "has no code style.")

    def test_has_user_class_doc(self):
        """
        Check if the User module has a docstring.
        """
        self.assertIsNot(User_Holder.__doc__, None,
                         "User has no docstring")
        self.assertTrue(len(User_Holder.__doc__) >= 1,
                        "User has no docstring")

    def test_user_has_func_docs(self):
        """
        Validate documentation for methods in the User class.
        """
        for fun_grapper in self.user_f:
            self.assertIsNot(fun_grapper[1].__doc__, None,
                             "{:s} method needs a docstring style".format(fun_grapper[0]))
            self.assertTrue(len(fun_grapper[1].__doc__) >= 1,
                            "{:s} method needs a docstring style".format(fun_grapper[0]))


class Test_User_class_docu(unittest.TestCase):
    """
    Test suite for functionality and documentation in the User class.
    """

    def test_user_is_subclass(self):
        """
        Validate if User is a subclass of BaseModel.
        """
        user_grapper = User_Holder()
        self.assertIsInstance(user_grapper, BaseModel)
        self.assertTrue(hasattr(user_grapper, "id"))
        self.assertTrue(hasattr(user_grapper, "created_at"))
        self.assertTrue(hasattr(user_grapper, "updated_at"))

    def test_user_email(self):
        """
        Validate the existence and default value of 'email' attribute in User class.
        """
        user_grapper = User_Holder()
        self.assertTrue(hasattr(user_grapper, "email"))
        self.assertEqual(user_grapper.email, "")

    def test_user_password(self):
        """
        Validate the existence and default value of 'password' attribute in User class.
        """
        user_grapper = User_Holder()
        self.assertTrue(hasattr(user_grapper, "password"))
        self.assertEqual(user_grapper.password, "")

    def test_user_fname(self):
        """
        Validate the existence and default value of 'first_name' attribute in User class.
        """
        user_grapper = User_Holder()
        self.assertTrue(hasattr(user_grapper, "fname"))
        self.assertEqual(user_grapper.first_name, "")

    def test_user_lname(self):
        """
        Validate the existence and default value of 'last_name' attribute in User class.
        """
        user_grapper = User_Holder()
        self.assertTrue(hasattr(user_grapper, "lname"))
        self.assertEqual(user_grapper.last_name, "")

    def test_to_dict_user_create(self):
        """
        Validate the creation of a dictionary representation of a User instance.
        """
        user_grapper = User_Holder()
        new_dictionery = user_grapper.to_dict()
        self.assertEqual(type(new_dictionery), dict)
        for has_entity in user_grapper.__dict__:
            self.assertTrue(has_entity in new_dictionery)
            self.assertTrue("__class__" in new_dictionery)

    def test_to_dict_user_val(self):
        """
        Validate the values of attributes in the dictionary representation of a User instance.
        """
        time_and_date_holder = "%Y-%m-%dT%H:%M:%S.%f"
        user_grapper = User_Holder()
        new_dictionery = user_grapper.to_dict()
        self.assertEqual(new_dictionery["__class__"], "User")
        self.assertEqual(type(new_dictionery["created_at"]), str)
        self.assertEqual(type(new_dictionery["updated_at"]), str)
        self.assertEqual(new_dictionery["created_at"], user_grapper.created_at.strftime(time_and_date_holder))
        self.assertEqual(new_dictionery["updated_at"], user_grapper.updated_at.strftime(time_and_date_holder))

    def test_user_str(self):
        """
        Validate the string representation of a User instance.
        """
        user_grapper = User_Holder()
        str_coll = "[User] ({}) {}".format(user_grapper.id, user_grapper.__dict__)
        self.assertEqual(str_coll, str(user_grapper))
