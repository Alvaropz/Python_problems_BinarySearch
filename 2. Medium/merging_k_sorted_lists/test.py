import unittest

from merging_k_sorted_lists import merging_k_sorted_lists, merging_k_sorted_lists_right_way

class TestCases(unittest.TestCase):
    def test_merging_k_sorted_lists(self):
        self.assertEqual(merging_k_sorted_lists([[],[],[10,12],[],[3,3,13],[3],[10],[0,7]]), [0, 3, 3, 3, 7, 10, 10, 12, 13])
        self.assertEqual(merging_k_sorted_lists([[],[],[]]), [])
        self.assertEqual(merging_k_sorted_lists([[1,2],[3,4],[5,6],[7,8],[9,10]]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(merging_k_sorted_lists([[4,7,9,6,5,8,4,3,4,6],[1],[0,9,7,6,5,4,6,7,3,5,6,8,2,1,34,5,67,8]]), [0, 1, 1, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6,6,6,6,6,7,7,7,8,8,8,9,9,34,67])

    def test_merging_k_sorted_lists_right_way(self):
        self.assertEqual(merging_k_sorted_lists_right_way([[],[],[10,12],[],[3,3,13],[3],[10],[0,7]]), [0, 3, 3, 3, 7, 10, 10, 12, 13])
        self.assertEqual(merging_k_sorted_lists_right_way([[],[],[]]), [])
        self.assertEqual(merging_k_sorted_lists_right_way([[1,2],[3,4],[5,6],[7,8],[9,10]]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(merging_k_sorted_lists_right_way([[4,7,9,6,5,8,4,3,4,6],[1],[0,9,7,6,5,4,6,7,3,5,6,8,2,1,34,5,67,8]]), [0, 1, 4, 7, 9, 6, 5, 8, 4, 3, 4, 6, 9, 7, 6, 5, 4, 6, 7, 3, 5, 6, 8, 2, 1, 34, 5, 67, 8])


if __name__ == "__main__":
    unittest.main(verbosity=2)