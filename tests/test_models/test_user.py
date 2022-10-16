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


class TestUser(unittest.TestCase):
    """tests for user"""

    def test_1(self):
        usuarin = User()
        self.assertEquals(usuarin.__class__.__name__, "User")

    def test_2(self):
        usuarin = User()
        self.assertTrue(type(usuarin.email) is str)
        self.assertTrue(type(usuarin.password) is str)
        self.assertTrue(type(usuarin.first_name) is str)
        self.assertTrue(type(usuarin.last_name) is str)
