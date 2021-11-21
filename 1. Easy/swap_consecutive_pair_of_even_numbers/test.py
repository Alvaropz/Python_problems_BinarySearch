import unittest

from swap_consecutive_pair_of_even_numbers import swap_consecutive_pair_of_even_numbers

class TestCases(unittest.TestCase):
    def test_swap_consecutive_pair_of_even_numbers(self):
        self.assertEqual(swap_consecutive_pair_of_even_numbers([2, 3, 4, 6, 8]), [4, 3, 2, 8, 6])
        self.assertEqual(swap_consecutive_pair_of_even_numbers([1, 3, 5, 7]), [1, 3, 5, 7])
        self.assertEqual(swap_consecutive_pair_of_even_numbers([2, 4, 6, 8, 10]), [4, 2, 8, 6, 10])

if __name__ == "__main__":
    unittest.main(verbosity=2)