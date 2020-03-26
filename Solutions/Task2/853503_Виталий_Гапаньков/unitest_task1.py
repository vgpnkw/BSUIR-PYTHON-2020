import lab2_task1
import unittest

class SortingTest(unittest.TestCase):
	def find_if_file_can_be_sorted(self):
		with open('sortfile.txt', 'w') as file:
			file.writelines('{}\n'.format(random.randint(1,1000000)) for _ in range(int(100)))

		with self.assertRaises(Exception):
			sort.splitFiles("digit.txt",10)
			sort.mergeSortedtemplefiles()

	def test_sort(self):
		list1 = [5,3,22,4,9,23,20]
		list2 = list1
		sort.externamMergeSort().mergeSort(list2)
		self.assertEqual(list2,sorted(list1))