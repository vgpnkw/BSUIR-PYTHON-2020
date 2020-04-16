import unittest
from lab2_task3 import Vector

class MyTestCase(unittest.TestCase):
    def test_input(self):
        self.assertEqual(str(Vector(["vor", 2])), '2')

    def test_sum(self):
        vector1 = Vector([-3, 4, 5, 10])
        vector2 = Vector([0, 7, 2, 3])
        self.assertEqual(vector1.sum(vector2), '-3, 11, 7, 13')

    def test_error_sum(self):
        vector1 = Vector([-3, 4, 5, 10, 18])
        vector2 = Vector([0, 7, 2, 3])
        self.assertEqual(vector1.sum(vector2), None)


    def test_sub(self):
        vector1 = Vector([-3, 4, 5, 10])
        vector2 = Vector([0, 7, 2, 3])
        self.assertEqual(vector1.sub(vector2), '-3, -3, 3, 7')

    def test_error_sub(self):
        vector1 = Vector([-3, 4, 5, 10, 18])
        vector2 = Vector([0, 7, 2, 3])
        self.assertEqual(vector1.sub(vector2), None)

    def test_mul_const(self):
        vec1 = Vector([-3, 4, 5, 10])
        self.assertEqual(vec1.mul_const(2), '-6, 8, 10, 20')

    def test_mul_scal(self):
        vec1 = Vector([-3, 4, 5, 10])
        vec2 = Vector([0, 7, 2, 3])
        self.assertEqual(vec1.mul_scal(vec2), 68)

    def test_error_mul_scal(self):
        vec1 = Vector([-3, 4, 5, 10, 11])
        vec2 = Vector([0, 7, 2, 3])
        self.assertEqual(vec1.mul_scal(vec2), None)

    def test_mul_compare_false(self):
        vec1 = Vector([-3, 4, 5, 10])
        vec2 = Vector([0, 7, 2, 3])
        self.assertFalse(vec1.compare(vec2))

    def test_error_mul_compare_false(self):
        vec1 = Vector([-3, 4, 5, 10, 11])
        vec2 = Vector([0, 7, 2, 3])
        self.assertEqual(vec1.compare(vec2), None)

    def test_mul_compare_true(self):
        vec1 = Vector([-3, 4, 5, 10])
        self.assertTrue(vec1.compare(vec1))

    def test_lenght(self):
        def test_length(self):
            vec1 = Vector([2, 2, 2, 2])
            self.assertEqual(vec1.len(), 4)
            vec1.length()
            self.assertEqual(vec1.length(), 4)

if __name__ == '__main__':
    unittest.main()
