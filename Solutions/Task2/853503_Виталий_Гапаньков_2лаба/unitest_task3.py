import unittest
from lab2_task3 import Vector

class MyTestCase(unittest.TestCase):
    def test_sum(self):
        vector1 = Vector([4, -5, 9, 7])
        vector2 = Vector([3, 6, -4, 2])
        self.assertEqual(vector1.sum(vector2), '7, 1, 5, 9')

    def test_sub(self):
        vector1 = Vector([4, -5, 9, 7])
        vector2 = Vector([3, 6, -4, 2])
        self.assertEqual(vector1.sub(vector2), '4, -5, 9, 7')

unittest.main()