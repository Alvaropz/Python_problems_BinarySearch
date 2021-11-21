import unittest

from recursive_index import recursive_index

class TestCases(unittest.TestCase):
    def test_recursive_index(self):
        self.assertEqual(recursive_index([1, 2, 3, 4, 5], 0), 5)
        self.assertEqual(recursive_index([4, 2, 1, 1, 1], 3), -1)
        self.assertEqual(recursive_index([5, 2, 1, 2, 1], 2), -1)
        self.assertEqual(recursive_index([1, 3, 5, 7], 2), 1)
        self.assertEqual(recursive_index([1, 3, 5, 7, 9, 10, 12, 14, 16, 18, 20], 7), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)