import unittest

from arithmetic_sequence_permutation import arithmetic_sequence_permutation, arithmetic_sequence_permutation_optimised

class TestCases(unittest.TestCase):
    def test_arithmetic_sequence_permutation(self):
        self.assertEqual(arithmetic_sequence_permutation([7, 1, 5, 3]), True)
        self.assertEqual(arithmetic_sequence_permutation([2, 4, 8, 16]), False)
        self.assertEqual(arithmetic_sequence_permutation([99, 90, 108, 81, 117, 72, 126, 63]), True)
        self.assertEqual(arithmetic_sequence_permutation([100, 75, 50, 25, 0]), True)
        self.assertEqual(arithmetic_sequence_permutation([0, 0]), True)
        self.assertEqual(arithmetic_sequence_permutation([1, 1, 2]), False)
        self.assertEqual(arithmetic_sequence_permutation([1, 100]), True)

    def test_arithmetic_sequence_permutation_optimised(self):
        self.assertEqual(arithmetic_sequence_permutation_optimised([7, 1, 5, 3]), True)
        self.assertEqual(arithmetic_sequence_permutation_optimised([2, 4, 8, 16]), False)
        self.assertEqual(arithmetic_sequence_permutation_optimised([99, 90, 108, 81, 117, 72, 126, 63]), True)
        self.assertEqual(arithmetic_sequence_permutation_optimised([100, 75, 50, 25, 0]), True)
        self.assertEqual(arithmetic_sequence_permutation_optimised([0, 0]), True)
        self.assertEqual(arithmetic_sequence_permutation_optimised([1, 1, 2]), False)
        self.assertEqual(arithmetic_sequence_permutation_optimised([1, 100]), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)