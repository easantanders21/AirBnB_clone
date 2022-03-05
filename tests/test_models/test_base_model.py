#!/usr/bin/python3
"""Test module"""

import unittest
from models.base_model import BaseModel
import datetime
import os


class TestBaseModel(unittest.TestCase):
    """New class to test class BaseModel"""
    list_met = [BaseModel.__init__, BaseModel.__str__,
                BaseModel.save, BaseModel.to_dict]

    def setUp(self):
        """create a instance"""

    def test_doc_class(self):
        """Test if the class documentation exist"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_doc_method(self):
        """Test if the method documentation exist"""
        for met in self.list_met:
            self.assertTrue(len(met.__doc__) > 0)

    def test_is_an_instance(self):
        """Test if a object is instance"""
        new_object = BaseModel()
        self.assertIsInstance(new_object, BaseModel)

    def test_att_in_class(self):
        """Test if a attr is in class"""
        new_object = BaseModel()
        self.assertTrue(hasattr(new_object, 'id'))
        self.assertTrue(hasattr(new_object, 'updated_at'))
        self.assertTrue(hasattr(new_object, 'created_at'))

    def test_str(self):
        """Test str function"""
        new_object = BaseModel()
        str_test = "[BaseModel] ({}) {}".format(new_object.id,
                                                new_object.__dict__)
        self.assertEqual(str_test, new_object.__str__())

    def test_save(self):
        """ Test that info is saved to file. """
        new_object = BaseModel()
        new_object.save()
        with open("file.json", 'r') as f:
            self.assertIn(new_object.id, f.read())

    def test_constructor_kwargs(self):
        """
        - Test constructor that has kwargs as attributes values.
        """
        new_object = BaseModel()
        new_dict = new_object.to_dict()
        new_object2 = BaseModel(**new_dict)

        self.assertIsInstance(new_object2, BaseModel)
        self.assertIsInstance(new_dict, dict)
        self.assertIsNot(new_object, new_object2)

    def test_uuid(self):
        """check if two ids are the same"""
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        self.assertNotEqual(obj_1.id, obj_2)


if __name__ == '__main__':
    unittest.main()
