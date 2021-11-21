import unittest

from sort_list_by_hamming_weight import sort_list_by_hamming_weight

class TestCases(unittest.TestCase):
    def test_sort_list_by_hamming_weight(self):
        self.assertEqual(sort_list_by_hamming_weight([3, 1, 4, 7]), [1, 4, 3, 7])
        self.assertEqual(sort_list_by_hamming_weight([0, 1, 2, 3, 4]), [0, 1, 2, 4, 3])
        self.assertEqual(sort_list_by_hamming_weight([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]), [1, 3, 5, 9, 17, 7, 11, 13, 19, 15])
        self.assertEqual(sort_list_by_hamming_weight([3, 3, 3, 3, 4, 4, 4, 4]), [4, 4, 4, 4, 3, 3, 3, 3])

if __name__ == "__main__":
    unittest.main(verbosity=2)