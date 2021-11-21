import unittest

from first_missing_positive_sequel import first_missing_positive_sequel, first_missing_positive_sequel_optimised

class TestCases(unittest.TestCase):
    def test_first_missing_positive_sequel(self):
        self.assertEqual(first_missing_positive_sequel([0, 1]), 2)
        self.assertEqual(first_missing_positive_sequel([0, 1, 2, 3, 5]), 4)
        self.assertEqual(first_missing_positive_sequel([1, 2, 3, 4, 5, 6]), 7)
        self.assertEqual(first_missing_positive_sequel([1, 2, 3, 5, 6]), 4)
        self.assertEqual(first_missing_positive_sequel([1, 2, 3, 4, 6, 7, 8, 9]), 5)
        self.assertEqual(first_missing_positive_sequel([2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)

    def test_first_missing_positive_sequel_optimised(self):
        self.assertEqual(first_missing_positive_sequel_optimised([0, 1]), 2)
        self.assertEqual(first_missing_positive_sequel_optimised([0, 1, 2, 3, 5]), 4)
        self.assertEqual(first_missing_positive_sequel_optimised([1, 2, 3, 4, 5, 6]), 7)
        self.assertEqual(first_missing_positive_sequel_optimised([1, 2, 3, 5, 6]), 4)
        self.assertEqual(first_missing_positive_sequel_optimised([1, 2, 3, 4, 6, 7, 8, 9]), 5)
        self.assertEqual(first_missing_positive_sequel_optimised([2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)