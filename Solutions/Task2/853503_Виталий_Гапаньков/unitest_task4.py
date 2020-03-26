import unittest
from  lab2_task4 import cached
from  lab2_task4 import multiplication
from  lab2_task4 import plusandpowl

class CachedTest(unittest.TestCase):
	def test_right_answer(self):
		self.assertEqual(int(multiplication(8, 4)), 32)


	def test_right_answer(self):
		self.assertEqual(int(plusandpowl(2, 2, 2)), 16.0)

unittest.main()