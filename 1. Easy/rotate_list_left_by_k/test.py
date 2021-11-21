import unittest

from rotate_list_left_by_k import rotate_list_by_k_less, rotate_list_by_k_optimised

class TestCases(unittest.TestCase):
    def test_rotate_less(self):
        self.assertEqual(rotate_list_by_k_less([1, 2, 3, 4, 5, 6], 2), [3, 4, 5, 6, 1, 2])
        self.assertEqual(rotate_list_by_k_less([1], 0), [1])
        self.assertEqual(rotate_list_by_k_less([1, 2, 3, 4, 5, 6], 4), [5, 6, 1, 2, 3, 4])
        self.assertEqual(rotate_list_by_k_less([30, 41, 56, 77, 14, 98], 5), [98, 30, 41, 56, 77, 14])
        self.assertEqual(rotate_list_by_k_less([6, 7, 8, 8, 9, 10], 6), [6, 7, 8, 8, 9, 10])
        self.assertEqual(rotate_list_by_k_less([1, 2, 4, 4], 3), [4, 1, 2, 4])

    def test_rotate_optimised(self):
        self.assertEqual(rotate_list_by_k_optimised([1, 2, 3, 4, 5, 6], 2), [3, 4, 5, 6, 1, 2])
        self.assertEqual(rotate_list_by_k_optimised([1], 0), [1])
        self.assertEqual(rotate_list_by_k_optimised([1, 2, 3, 4, 5, 6], 4), [5, 6, 1, 2, 3, 4])
        self.assertEqual(rotate_list_by_k_optimised([30, 41, 56, 77, 14, 98], 5), [98, 30, 41, 56, 77, 14])
        self.assertEqual(rotate_list_by_k_optimised([6, 7, 8, 8, 9, 10], 6), [6, 7, 8, 8, 9, 10])
        self.assertEqual(rotate_list_by_k_optimised([1, 2, 4, 4], 3), [4, 1, 2, 4])

if __name__ == "__main__":
    unittest.main(verbosity=2)