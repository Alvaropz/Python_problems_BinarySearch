import unittest

from append_list_to_sum_target import append_list_to_sum_target, append_list_to_sum_target_optimised

class TestCases(unittest.TestCase):
    def test_append_list_to_sum_target(self):
        self.assertEqual(append_list_to_sum_target([2, 1], 3, 10), 3)
        self.assertEqual(append_list_to_sum_target([2, 1], 2, -4), 4)
        self.assertEqual(append_list_to_sum_target([2, 1, 5, 6], 4, 60), 12)
        self.assertEqual(append_list_to_sum_target([1, 0], 1, 0), 1)
        self.assertEqual(append_list_to_sum_target([1, 0], 2, -3), 2)
        self.assertEqual(append_list_to_sum_target([1, 0, 5, 10], 5, -20), 8)

    def test_append_list_to_sum_target_optimised(self):
        self.assertEqual(append_list_to_sum_target_optimised([2, 1], 3, 10), 3)
        self.assertEqual(append_list_to_sum_target_optimised([2, 1], 2, -4), 4)
        self.assertEqual(append_list_to_sum_target_optimised([2, 1, 5, 6], 4, 60), 12)
        self.assertEqual(append_list_to_sum_target_optimised([1, 0], 1, 0), 1)
        self.assertEqual(append_list_to_sum_target_optimised([1, 0], 2, -3), 2)
        self.assertEqual(append_list_to_sum_target_optimised([1, 0, 5, 10], 5, -20), 8)

if __name__ == "__main__":
    unittest.main(verbosity=2)