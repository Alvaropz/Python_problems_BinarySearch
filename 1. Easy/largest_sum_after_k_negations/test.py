import unittest

from largest_sum_after_k_negations import largest_sum_after_k_negations

class TestCases(unittest.TestCase):
    def test_largest_sum_after_k_negations(self):
        self.assertEqual(largest_sum_after_k_negations([1, 0, -5, -3], 4), 9)
        self.assertEqual(largest_sum_after_k_negations([0, 1, 2], 7), 3)
        self.assertEqual(largest_sum_after_k_negations([0, -1, -2], 5), 3)
        self.assertEqual(largest_sum_after_k_negations([0, -1, -2], 6), 3)
        self.assertEqual(largest_sum_after_k_negations([0, 0, 0, 0], 4), 0)
        self.assertEqual(largest_sum_after_k_negations([0, 0, 0, 0], 3), 0)
        self.assertEqual(largest_sum_after_k_negations([1, 1], 4), 2)
        self.assertEqual(largest_sum_after_k_negations([1, 1], 9), 0)
        self.assertEqual(largest_sum_after_k_negations([-5, -4, -3, -2, -1], 8), 13)


if __name__ == "__main__":
    unittest.main(verbosity=2)