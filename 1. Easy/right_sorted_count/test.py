import unittest

from right_sorted_count import right_sorted

class TestCases(unittest.TestCase):
    def test_sorted(self):
        self.assertEqual(right_sorted([1, 7, 3, 4, 10]), 2)
        self.assertEqual(right_sorted([1, 2, 3, 4, 5]), 5)
        self.assertEqual(right_sorted([5, 4, 3, 2, 1]), 1)
        self.assertEqual(right_sorted([]), 0)
        self.assertEqual(right_sorted([9, 7, 4, 3, 2, 1, 5, 7, 8]), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)