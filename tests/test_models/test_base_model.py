#!/usr/bin/python3
"""Unittest moment"""

import unittest
from models.base_model import BaseModel
import datetime

class TestBase(unittest.TestCase):
    """aaaaa"""
    
    def tryaa(self):
        """aaaaaa"""
        basesita = BaseModel()
        self.assertEqual(type(basesita.id), str, [])
        self.assertEqual(type(basesita.created_at), datetime)
        self.assertEqual(type(basesita.updated_at), datetime)

