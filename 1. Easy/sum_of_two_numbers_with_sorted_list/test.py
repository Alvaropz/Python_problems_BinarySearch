import unittest

from sum_of_two_numbers_with_sorted_list import sum_of_two_numbers_with_sorted_list, sum_of_two_numbers_with_sorted_list_optimised

class TestCases(unittest.TestCase):
    def test_sum_of_two_numbers_with_sorted_list(self):
        self.assertEqual(sum_of_two_numbers_with_sorted_list([1, 3, 5, 8], 6), True)
        self.assertEqual(sum_of_two_numbers_with_sorted_list([1, 3, 4, 8], 6), False)
        self.assertEqual(sum_of_two_numbers_with_sorted_list([0], 0), False)
        self.assertEqual(sum_of_two_numbers_with_sorted_list([0, 0], 0), True)
        self.assertEqual(sum_of_two_numbers_with_sorted_list([0, -1], 0), False)
        self.assertEqual(sum_of_two_numbers_with_sorted_list([1, 1], 0), False)

    def test_sum_of_two_numbers_with_sorted_list_optimised(self):
        self.assertEqual(sum_of_two_numbers_with_sorted_list_optimised([1, 3, 5, 8], 6), True)
        self.assertEqual(sum_of_two_numbers_with_sorted_list_optimised([1, 3, 4, 8], 6), False)
        self.assertEqual(sum_of_two_numbers_with_sorted_list_optimised([0], 0), False)
        self.assertEqual(sum_of_two_numbers_with_sorted_list_optimised([0, 0], 0), True)
        self.assertEqual(sum_of_two_numbers_with_sorted_list_optimised([0, -1], 0), False)
        self.assertEqual(sum_of_two_numbers_with_sorted_list_optimised([1, 1], 0), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)