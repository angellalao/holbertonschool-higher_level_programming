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
        """converts list to json string, returns json string"""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")
        json_str2 = Base.to_json_string([])
        self.assertEqual(json_str2, "[]")
        dict_list3 = [ { 'id': 12 }]
        json_str3 = Base.to_json_string(dict_list3)
        self.assertEqual(json_str3, '[{"id": 12}]')

    def test_from_json_string(self):
        """converts json string to list, returns list """
        dict_list = Base.from_json_string(None)
        self.assertEqual(dict_list, [])
        dict_list2 = Base.from_json_string("[]")
        self.assertEqual(dict_list2, [])
        json_str3 = '[{ "id": 89 }]'
        dict_list3 = Base.from_json_string(json_str3)
        self.assertEqual(dict_list3, [{ "id": 89 }])
 
