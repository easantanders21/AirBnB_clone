#!/usr/bin/python3
"""Test module"""


import unittest
from models.state import State


class TestMyState(unittest.TestCase):
    """New class to test class State"""

    def setUp(self):
        """Setting up"""
        self.obj_state = State()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.obj_state

    def test_is_instance(self):
        """Check if an instance belongs to class State"""
        self.assertIsInstance(self.obj_state, State)

    def test_if_str(self):
        """Check if the attribute is str"""
        self.assertIsInstance(self.obj_state.name, str)

    def test_is_an_instance(self):
        """Check if my_model is an instance of BaseModel"""
        self.assertIsInstance(self.obj_state, State)

    def test_module_doc(self):
        """ Method to check for module documentation."""
        self.assertTrue(len(self.obj_state.__doc__) > 0)

    def test_method_docs(self):
        """ Method to check for method´s documentation."""
        for func in dir(State):
            self.assertTrue(len(func.__doc__) > 0)

if __name__ == '__main__':
    unittest.main()
