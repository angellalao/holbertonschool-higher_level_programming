#!/usr/bin/python3
"""
Unittest for base module
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ """
    def test_id(self):
        """assigns new id to instance when create"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertNotEqual(b1.id, b2.id)

    def test_existing_id(self):
        """saves existing id"""
        b1 = Base(45)
        self.assertEqual(b1.id, 45)

    def test_to_json_string(self):
        pass
    
    def test_from_json_string(self):
        pass
