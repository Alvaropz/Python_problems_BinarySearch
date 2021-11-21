import unittest

from pair_sums import pair_sums, pair_sums_optimised

class TestCases(unittest.TestCase):
    def test_pair_sums(self):
        self.assertEqual(pair_sums([3, 2, 4]), 2)
        self.assertEqual(pair_sums([1, 1, 1]), 0)
        self.assertEqual(pair_sums([5, 2, 4, 6, 1, 3]), 9)
        self.assertEqual(pair_sums([0, 1]), 1)

    def test_pair_sums_optimised(self):
        self.assertEqual(pair_sums_optimised([3, 2, 4]), 2)
        self.assertEqual(pair_sums_optimised([1, 1, 1]), 0)
        self.assertEqual(pair_sums_optimised([5, 2, 4, 6, 1, 3]), 9)
        self.assertEqual(pair_sums_optimised([0, 1]), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)