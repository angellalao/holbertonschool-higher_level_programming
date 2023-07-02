#!/usr/bin/python3

"""Module for testing Square class"""
import unittest
from models.square import Square
from models.base import Base
import io
import sys
import os

class TestSquare(unittest.TestCase):
     """test for variable arguments used with Square class """
     def test_square_args(self):
         """test for creating square instance with variable arguments"""
         s1 = Square(1)
         self.assertEqual(s1.size, 1)
         self.assertEqual(s1.x, 0)
         self.assertEqual(s1.y, 0)
         s2 = Square(1, 2)
         self.assertEqual(s2.size, 1)
         self.assertEqual(s2.x, 2)
         self.assertEqual(s2.y, 0)
         s3 = Square(1, 2, 3)
         self.assertEqual(s3.size, 1)
         self.assertEqual(s3.x, 2)
         self.assertEqual(s3.y, 3)
         s4 = Square(1, 2, 3, 4)
         self.assertEqual(s4.size, 1)
         self.assertEqual(s4.x, 2)
         self.assertEqual(s4.y, 3)
         self.assertEqual(s4.id, 4)

     def test_square_str_args(self):
          """test for error raised with type string arguments"""
          with self.assertRaises(TypeError):
               s1 = Square("1")
          with self.assertRaises(TypeError):
               s2 = Square(1, "2")
          with self.assertRaises(TypeError):
               s3 = Square(1, 2, "3")

     def test_square_negative_args(self):
          """test for error raised with negative int arguments"""
          with self.assertRaises(ValueError):
               s1 = Square(-1, 2)
          with self.assertRaises(ValueError):
               s2 = Square(1, -2)
          with self.assertRaises(ValueError):
               s3 = Square(1, 2, -3)
          with self.assertRaises(ValueError):
               s5 = Square(0)

     def test_area(self):
          """test for calculating area of square """
          s1 = Square(1, 3, 4, 5)
          self.assertEqual(s1.area(), 1)

     def test_str(self):
          """string printed when str() or print() are used"""
          s1 = Square(1, 2, 3, 4)
          self.assertEqual(str(s1), "[Square] (4) 2/3 - 1")

     def test_square_display(self):
          """the string method delivers expected custom message"""
          out = io.StringIO()
          sys.stdout = out
          s1 = Square(1)
          s1.display()
          sys.stdout = sys.__stdout__
          self.assertEqual(out.getvalue(), "#\n")
