#!/usr/bin/python3
"""Test module Place"""


from models.base_model import BaseModel
from models.place import Place
import unittest
import datetime
import os


class TestAmenity(unittest.TestCase):
    """New class to test class Place"""

    def test_doc_class(self):
        """Test if the class documentation exist"""
        self.assertTrue(len(Place.__doc__) > 0)

    def test_is_an_instance(self):
        """Test if a object is instance"""
        new_object = Place()
        self.assertIsInstance(new_object, Place)

    def test_att_in_class(self):
        """Test if a attr is in class"""
        new_object = Place()
        self.assertTrue(hasattr(new_object, 'id'))
        self.assertTrue(hasattr(new_object, 'updated_at'))
        self.assertTrue(hasattr(new_object, 'created_at'))
        self.assertTrue(hasattr(new_object, 'city_id'))
        self.assertTrue(hasattr(new_object, 'user_id'))
        self.assertTrue(hasattr(new_object, 'name'))
        self.assertTrue(hasattr(new_object, 'description'))
        self.assertTrue(hasattr(new_object, 'number_rooms'))
        self.assertTrue(hasattr(new_object, 'number_bathrooms'))
        self.assertTrue(hasattr(new_object, 'max_guest'))
        self.assertTrue(hasattr(new_object, 'price_by_night'))
        self.assertTrue(hasattr(new_object, 'latitude'))
        self.assertTrue(hasattr(new_object, 'longitude'))
        self.assertTrue(hasattr(new_object, 'amenity_ids'))

    def test_type_att(self):
        """Test if a attr is type"""
        new_object = Place()
        self.assertIsInstance(new_object.city_id, str)
        self.assertIsInstance(new_object.user_id, str)
        self.assertIsInstance(new_object.name, str)
        self.assertIsInstance(new_object.description, str)
        self.assertIsInstance(new_object.number_rooms, int)
        self.assertIsInstance(new_object.number_bathrooms, int)
        self.assertIsInstance(new_object.max_guest, int)
        self.assertIsInstance(new_object.price_by_night, int)
        self.assertIsInstance(new_object.latitude, float)
        self.assertIsInstance(new_object.longitude, float)
        self.assertIsInstance(new_object.amenity_ids, list)

    def test_subclass(self):
        """Test to check the inheritance"""
        new_object = Place()
        self.assertTrue(issubclass(new_object.__class__, BaseModel))

    def test_obj_from_dic(self):
        """Test create new obj from dic"""
        new_object = Place()
        dict_new_object = new_object.to_dict()
        new_object2 = Place(**dict_new_object)
        self.assertIsInstance(new_object2, Place)
        self.assertTrue(issubclass(new_object2.__class__, BaseModel))
        self.assertIsNot(new_object, new_object2)


if __name__ == '__main__':
    unittest.main()
