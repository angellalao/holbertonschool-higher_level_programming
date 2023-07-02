#!/usr/bin/python3
"""
Unittest for base module
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ """
    def test_id(self):
        """assigns new id to instance, unless id specified when created"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertNotEqual(b1.id, b2.id)
        b3 = Base(45)
        self.assertEqual(b3.id, 45)

    def test_to_json_string(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")
        json_str2 = Base.to_json_string([])
        self.assertEqual(json_str2, "[]")
        dict_list3 = [ { 'id': 12 }]
        json_str3 = Base.to_json_string(dict_list3)
        self.assertEqual(json_str3, '[{"id": 12}]')
    
    def test_from_json_string(self):
        pass
