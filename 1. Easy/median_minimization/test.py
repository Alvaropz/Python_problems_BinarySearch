import unittest

from median_minimization import median_minimization

class TestCases(unittest.TestCase):
    def test_median_minimization(self):
        self.assertEqual(median_minimization([1, 9, 7, 4, 3, 6]), 2)
        self.assertEqual(median_minimization([6, 10, 8, 1, 7, 5]), 1)
        self.assertEqual(median_minimization([1, 2]), 1)
        self.assertEqual(median_minimization([2, 1, 4, 3, 6, 5, 8, 7]), 1)
        self.assertEqual(median_minimization([60, 50, 40, 3, 2, 1]), 37)
        self.assertEqual(median_minimization([25, 24, 23, 22, 11, 10, 9, 8, 7, 6]), 1)
        self.assertEqual(median_minimization([100, 1]), 99)

if __name__ == "__main__":
    unittest.main(verbosity=2)