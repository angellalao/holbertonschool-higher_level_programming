import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """test for variable arguments used with Square class """

    def test_square_args(self):
        """test for creating square instance with variable arguments"""
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
