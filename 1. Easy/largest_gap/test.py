import unittest

from largest_gap import largest_gap

class TestCases(unittest.TestCase):
    def test_largest_gap(self):
        self.assertEqual(largest_gap([4, 1, 2, 8, 9, 10]), 4)
        self.assertEqual(largest_gap([4, 1, 2, 8, 15]), 7)
        self.assertEqual(largest_gap([1, 2]), 1)
        self.assertEqual(largest_gap([1, 50]), 49)
        self.assertEqual(largest_gap([0, 1]), 1)
        self.assertEqual(largest_gap([0, 1, 2, 3, 4, 5, 7, 8, 9, 10]), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)