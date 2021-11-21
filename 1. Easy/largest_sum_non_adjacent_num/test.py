import unittest

from largest_sum_non_adjacent_num import largest_sum_non_adjacent_num

class TestCases(unittest.TestCase):
    def test_largest_sum_non_adjacent_num(self):
        self.assertEqual(largest_sum_non_adjacent_num([2, 4, 6, 2, 5]), 13)
        self.assertEqual(largest_sum_non_adjacent_num([5, 1, 1, 5]), 10)
        self.assertEqual(largest_sum_non_adjacent_num([2, 4, 6, 2, 5, 1, 1, 5]), 7)

if __name__ == "__main__":
    unittest.main(verbosity=2)