#!/usr/bin/python3
"""Unittest moment"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import datetime
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestPlace(unittest.TestCase):
    """tests for user"""

    def test_1(self):
        usuarin = Place()
        self.assertEquals(usuarin.__class__.__name__, "Place")

    def test_2(self):
        usuarin = Place()
        self.assertTrue(type(usuarin.city_id) is str)
        self.assertTrue(type(usuarin.user_id) is str)
        self.assertTrue(type(usuarin.name) is str)
        self.assertTrue(type(usuarin.description) is str)
        self.assertTrue(type(usuarin.number_rooms) is int)
        self.assertTrue(type(usuarin.number_bathrooms) is int)
        self.assertTrue(type(usuarin.max_guest) is int)
        self.assertTrue(type(usuarin.price_by_night) is int)
        self.assertTrue(type(usuarin.latitude) is float)
        self.assertTrue(type(usuarin.longitude) is float)
        self.assertTrue(type(usuarin.amenity_ids) is list[str])
