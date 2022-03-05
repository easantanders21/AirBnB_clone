#!/usr/bin/python3
"""New testing module"""


import unittest
from models.base_model import BaseModel
from models.user import User


class TestMyUser(unittest.TestCase):
    """Class TestMyUser to test class User"""

    def setUp(self):
        """setting up each test"""
        self.obj_user = User()
        self.obj_1 = BaseModel()
        self.obj_2 = BaseModel()

    def tearDown(self):
        """cleaning up after each test"""
        del self.obj_user
        del self.obj_1
        del self.obj_2

    def datatype(self):
        """cleaning up after each test"""
        self.assertTrue(hasattr(self.obj_user, "email"))
        self.assertEqual(type(self.obj_user.email), str)
        self.assertTrue(hasattr(self.obj_user, "password"))
        self.assertEqual(type(self.obj_user.password), str)
        self.assertTrue(hasattr(self.obj_user, "first_name"))
        self.assertEqual(type(self.obj_user.first_name), str)
        self.assertTrue(hasattr(self.obj_user, "last_name"))
        self.assertEqual(type(self.obj_user.last_name), str)

    def test_empty_strings_before(self):
        """Check if the strings are empty before assignment"""
        self.assertFalse(self.obj_user.email)
        self.assertFalse(self.obj_user.password)
        self.assertFalse(self.obj_user.first_name)
        self.assertFalse(self.obj_user.last_name)

    def test_methods_exist(self):
        """Check if the methods are present"""
        assert self.obj_user.__init__ is not None
        assert self.obj_user.save is not None
        assert self.obj_user.to_dict is not None
        assert self.obj_user.updated_at is not None
        assert self.obj_user.__str__ is not None

    def test_attributes_exist(self):
        """Assign attributes and check if they are not None"""
        self.obj_user.email = 'James.grijalba@holberton.com'
        self.obj_user.password = 'imsupercool'
        self.obj_user.first_name = 'Frank'
        self.obj_user.last_name = 'Grijalba'

        self.assertNotEqual(self.obj_user.email, None)
        self.assertNotEqual(self.obj_user.password, None)
        self.assertNotEqual(self.obj_user.first_name, None)
        self.assertNotEqual(self.obj_user.last_name, None)

    def test_attributes_are_correct(self):
        """Check if assigments happened as intended"""
        self.obj_user.email = 'James.grijalba@holberton.com'
        self.obj_user.password = 'imsupercool'
        self.obj_user.first_name = 'Frank'
        self.obj_user.last_name = 'Grijalba'

        self.assertEqual(self.obj_user.email, 'James.grijalba@holberton.com')
        self.assertEqual(self.obj_user.password, 'imsupercool')
        self.assertEqual(self.obj_user.first_name, 'Frank')
        self.assertEqual(self.obj_user.last_name, 'Grijalba')

    def test_if_str(self):
        """Check if the attributes are strings"""
        self.obj_user.email = 'James.grijalba@holberton.com'
        self.obj_user.password = 'imsupercool'
        self.obj_user.first_name = 'Frank'
        self.obj_user.last_name = 'Grijalba'

        self.assertTrue(type(self.obj_user.email) == str)
        self.assertTrue(type(self.obj_user.password) == str)
        self.assertTrue(type(self.obj_user.first_name) == str)
        self.assertTrue(type(self.obj_user.last_name) == str)

    def test_is_an_instance(self):
        """Check if my_model is an instance of BaseModel"""
        self.assertIsInstance(self.obj_user, User)

    def test_module_doc(self):
        """ Method to check for module documentation."""
        self.assertTrue(len(self.obj_user.__doc__) > 0)

    def test_method_docs(self):
        """ Method to check for method´s documentation."""
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == '__main__':
    unittest.main()
