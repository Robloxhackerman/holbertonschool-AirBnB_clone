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


class TestReview(unittest.TestCase):
    """tests for user"""

    def test_1(self):
        usuarin = Review()
        self.assertEquals(usuarin.__class__.__name__, "Review")
