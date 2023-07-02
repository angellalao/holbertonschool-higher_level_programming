"""unittest for rectangle module"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """ """
    def test_rectangle_args(self):
        """ """
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)
        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        r3 = Rectangle(1, 2, 3)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        r4 = Rectangle(1, 2)
        self.assertEqual(r4.width, 1)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 0)

    def test_rectangle_str_args(self):
        """ """
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 2, 3, "4")

    def test_rectangle_negative_args(self):
        """ """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 2, 3, -4)
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)

    def test_rectangle_area(self):
        """calculates area of rectangle"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.area(), 2)

    def test_str(self):
        """prints string when str() or print() invoked"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assetEqual(str(r1), "[Rectangle] (5) 3/4 - 1/2")

    def test_display(self):
        """prints representation of rectangle"""
        out = io.StringIO()
        sys.stdout = out
        r1 = Rectangle(1, 1, 1, 1)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "\n #\n")
