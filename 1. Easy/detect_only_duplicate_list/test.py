import unittest

from detect_only_duplicate_list import only_duplicate

class TestCases(unittest.TestCase):
    def test_only_duplicate(self):
        self.assertEqual(only_duplicate([1, 2, 3, 1]), 1)
        self.assertEqual(only_duplicate([1, 2, 4, 4]), 4)
        self.assertEqual(only_duplicate([2, 2]), 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)