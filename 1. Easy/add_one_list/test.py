import unittest

from add_one_list import add_one

class TestCases(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(add_one([1, 9, 1]), [1, 9, 2])
        self.assertEqual(add_one([9]), [1, 0])
        self.assertEqual(add_one([1, 9, 9]), [2, 0, 0])
        self.assertEqual(add_one([9, 9, 9, 9, 9, 9]), [1, 0, 0, 0, 0, 0, 0])

if __name__ == "__main__":
    unittest.main(verbosity=2)