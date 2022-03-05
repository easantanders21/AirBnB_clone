#!/usr/bin/python3
"""Test module"""


import unittest
from models.review import Review


class TestMyReview(unittest.TestCase):
    """New class to test class Review"""

    def setUp(self):
        """Setting up"""
        self.obj_review = Review()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.obj_review

    def test_is_instance(self):
        """Check if attributes are of a correct type"""
        self.assertIsInstance(self.obj_review, Review)

    def test_if_str(self):
        """Check if the attrs are str"""
        self.assertIsInstance(self.obj_review.place_id, str)
        self.assertIsInstance(self.obj_review.user_id, str)
        self.assertIsInstance(self.obj_review.text, str)

    def test_is_an_instance(self):
        """Check if my_model is an instance of BaseModel"""
        self.assertIsInstance(self.obj_review, Review)

    def test_module_doc(self):
        """ Method to check for module documentation."""
        self.assertTrue(len(self.obj_review.__doc__) > 0)

    def test_method_docs(self):
        """ Method to check for method´s documentation."""
        for func in dir(Review):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == '__main__':
    unittest.main()
