#!/usr/bin/python3
"""
Test suite for the Review module.
"""

from datetime import datetime
import pep8
import inspect
from models import review
from models.base_model import BaseModel
import unittest

"""Alias for better readability"""

Grapp_Review = review.Review

class TestReviewDocumentation(unittest.TestCase):
    """ Test Review Documentation"""
    @classmethod
    def setUpClass(cls):
        cls.review_f = inspect.getmembers(Grapp_Review, inspect.isfunction)

    def test_formatting_rule_review(self):
        """
        Ensure PEP8 formatting in the Review module.
        """
        formatter = pep8.StyleGuide(quiet=True)
        result_grapper = formatter.check_files(['models/review.py'])
        self.assertEqual(result_grapper.total_errors, 0, "Code style errors detected.")

    def test_formatting_rule_test_review(self):
        """
        Ensure PEP8 formatting in the test_review file.
        """
        formatter = pep8.StyleGuide(quiet=True)
        result_grapper = formatter.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result_grapper.total_errors, 0, "Code style errors detected.")

    def test_review_documentation(self):
        """
        Check if the Review module has documentation.
        """
        self.assertIsNot(review.__doc__, None, "Lacks Documentation")
        self.assertTrue(len(review.__doc__) >= 1, "Lacks Documentation")

    def test_review_class_documentation(self):
        """
        Check if the Review class has documentation.
        """
        self.assertIsNot(Grapp_Review.__doc__, None, "Lacks Documentation")
        self.assertTrue(len(Grapp_Review.__doc__) >= 1, "Lacks Documentation")

    def test_review_function_info(self):
        """
        Check if Review methods have documentation.
        """
        for rev_func in self.review_f:
            self.assertIsNot(rev_func[1].__doc__, None, "{:s} method Lacks Documentation".format(rev_func[0]))
            self.assertTrue(len(rev_func[1].__doc__) >= 1, "{:s} method Lacks Documentation".format(rev_func[0]))

class TestReviewFunctionality(unittest.TestCase):
    
    def test_review_is_subclass(self):
        """
        Check if Review is a subclass of BaseModel.
        """
        review_grapper = Grapp_Review()
        self.assertIsInstance(review_grapper, BaseModel)
        self.assertTrue(hasattr(review_grapper, "id"))
        self.assertTrue(hasattr(review_grapper, "created_at"))
        self.assertTrue(hasattr(review_grapper, "updated_at"))

    def test_place_has_user_id_attr(self):
        """
        Check if Review has the 'place_id' attribute.
        """
        review_grapper = Grapp_Review()
        self.assertTrue(hasattr(review_grapper, "place_id"))
        self.assertEqual(review_grapper.place_id, "")

    def test_user_id_entity_holder(self):
        """
        Check if Review has the 'user_id' attribute.
        """
        review_grapper = Grapp_Review()
        self.assertTrue(hasattr(review_grapper, "user_id"))
        self.assertEqual(review_grapper.user_id, "")

    def test_review_text_entity_attr(self):
        """
        Check if Review has the 'text' attribute.
        """
        review_grapper = Grapp_Review()
        self.assertTrue(hasattr(review_grapper, "text"))
        self.assertEqual(review_grapper.text, "")

    def test_to_dict_creates_dict(self):
        """
        Check if to_dict() creates a dictionary for Review.
        """
        review_grapper = Grapp_Review()
        new_dictionary_holder = review_grapper.to_dict()
        self.assertEqual(type(new_dictionary_holder), dict)
        for has_entity in review_grapper.__dict__:
            self.assertTrue(has_entity in new_dictionary_holder)
            self.assertTrue("__class__" in new_dictionary_holder)

    def test_to_dictionary_has_values(self):
        """
        Check if to_dict() includes the correct values for Review.
        """
        time_and_date_holder = "%Y-%m-%dT%H:%M:%S.%f"
        review_grapper = Grapp_Review()
        new_dictionary_holder = review_grapper.to_dict()
        self.assertEqual(new_dictionary_holder["__class__"], "Review")
        self.assertEqual(type(new_dictionary_holder["created_at"]), str)
        self.assertEqual(type(new_dictionary_holder["updated_at"]), str)
        self.assertEqual(new_dictionary_holder["created_at"], review_grapper.created_at.strftime(time_and_date_holder))
        self.assertEqual(new_dictionary_holder["updated_at"], review_grapper.updated_at.strftime(time_and_date_holder))

    def test_review_str_holder(self):
        """
        Check if str() representation is correctly formatted for Review.
        """
        review_grapper = Grapp_Review()
        string_holder = "[Review] ({}) {}".format(review_grapper.id, review_grapper.__dict__)
        self.assertEqual(string_holder, str(review_grapper))
