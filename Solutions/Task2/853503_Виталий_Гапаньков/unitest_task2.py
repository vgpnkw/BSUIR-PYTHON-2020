import unittest
from lab2_task2 import Json
import json
class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_json = Json()
        set = [228, False, 14.82, True, {5: "BSUIR1", 0: 28}, [88, 55]]
        self.assertEqual(my_json.to_json(set), json.dumps(set))

unittest.main()