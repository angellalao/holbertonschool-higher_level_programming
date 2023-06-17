#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([6, 2, 3, 4]), 6)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([6, 2, 10, 3, 4]), 10)
        self.assertAlmostEqual(max_integer([6, 2, -1, 4]), 6)
        self.assertAlmostEqual(max_integer([-6, -2, -3, -4]), -2)
        self.assertAlmostEqual(max_integer([5]), 5)
