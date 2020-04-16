import unittest
from lab2_task2 import Json
import json

class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_json = Json()
        set = [228, False, 14.82, True, {5: "BSUIR1", 0: 28}, [88, 55]]
        self.assertEqual(my_json.to_json(set), json.dumps(set))

    def test_1(self):
        my_json = Json()
        test = {"vor": 100}
        self.assertEqual(my_json.to_json(test), json.dumps(test))

    def test_2(self):
        my_json = Json()
        test = 100
        self.assertEqual(my_json.to_json(test), json.dumps(test))

    def test_3(self):
        my_json = Json()
        test = {"Univ": "Bsuir", "vor": [3, "str"]}
        self.assertEqual(my_json.to_json(test), json.dumps(test))

if __name__ == '__main__':
    unittest.main()

