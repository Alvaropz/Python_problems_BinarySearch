import unittest

from insertion_index_in_sorted_list import insertion_index_in_sorted_list

class TestCases(unittest.TestCase):
    def test_insertion_index_in_sorted_list(self):
        self.assertEqual(insertion_index_in_sorted_list([1,2,4,5], 3), 2)
        self.assertEqual(insertion_index_in_sorted_list([1,1,1,2,4,5], 1), 3)
        self.assertEqual(insertion_index_in_sorted_list([1], 0), 0)
        self.assertEqual(insertion_index_in_sorted_list([2], 0), 0)
        self.assertEqual(insertion_index_in_sorted_list([2], 3), 1)
        self.assertEqual(insertion_index_in_sorted_list([0, 2], 1), 1)
        self.assertEqual(insertion_index_in_sorted_list([0, 3], 2), 1)
        self.assertEqual(insertion_index_in_sorted_list([0, 1], 2), 2)
        self.assertEqual(insertion_index_in_sorted_list([1, 3], 0), 0)
        self.assertEqual(insertion_index_in_sorted_list([1,2,4,5], 6), 4)
        self.assertEqual(insertion_index_in_sorted_list([1,2,4,5], 0), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)