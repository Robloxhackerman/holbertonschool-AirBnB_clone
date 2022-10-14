#!/usr/bin/python3
"""Unittest moment"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import datetime

class TestBase(unittest.TestCase):
    """aaaaa"""

    def setUp(self):
        """aaaaa"""
        self.basesita = BaseModel()
    def test1(self):
        """aaaaaa"""
        self.assertEqual(type(self.basesita.id), str, [])
        self.assertEqual(type(self.basesita.created_at), datetime.datetime)
        self.assertEqual(type(self.basesita.updated_at), datetime.datetime)

    def test_initt(self):
        """tests init"""
        self.assertTrue(isinstance(self.basesita, BaseModel))

    def test_save(self):
        """tests save"""
        self.basesita.save()
        self.assertNotEqual(self.basesita.created_at, self.basesita.updated_at)


if __name__ == '__main__':
    unittest.main()
