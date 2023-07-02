"""unittest for square module"""
import unittest
from models.square import Square
import io
import os
import sys

class TestSquare(unittest.TestCase):
    """test for variable arguments used with Square class """
    def test_square_args(self):
        """ """
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)
        s2 = Square(1, 2)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.id, 2)
        s3 = Square(1, 2, 3)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.id, 3)
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

    def test_square_display_pos(self):
        """the string method delivers expected custom message"""
        out = io.StringIO()
        sys.stdout = out
        s1 = Square(1, 1, 1)
        s1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "\n #\n")

    def test_square_todictionary(self):
        """the square is converted to a dictionary"""
        s1 = Square(10, 1, 9, 22)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'x': 1, 'y': 9, 'id': 22, 'size': 10})

    def test_square_update(self):
        """update changes each argument for square"""
        s1 = Square(8, 8, 8, 8)
        s1.update(89)
        self.assertEqual(s1.id, 89)

    def test_square_create(self):
        """create new instance of square with args as parameters"""
        s1 = Square.create(**{ 'id': 89 })
        self.assertEqual(s1.id, 89)

    def test_square_save_to_file_none(self):
        """square save to file, read file contents are correct"""
        Square.save_to_file(None)
        with open("Square.json", 'r') as f2:
            s2 = f2.read()
        self.assertEqual(s2, '[]')
        os.remove("Square.json")

    def test_square_save_to_file_empty(self):
        """square save to file, read file contents are correct"""
        Square.save_to_file([])
        with open("Square.json", 'r') as f:
            s1 = f.read()
        self.assertEqual(s1, '[]')
        os.remove("Square.json")

    def test_square_load(self):
        """testing the load file method, expected rect back"""
        s1 = Square(10, 2, 8, 88)
        list_squares_input = [s1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[0]), '[Square] (88) 2/8 - 10')
        os.remove("Square.json")
