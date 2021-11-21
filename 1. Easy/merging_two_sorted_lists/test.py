import unittest

from merging_two_sorted_lists import merging_two_sorted_lists

class TestCases(unittest.TestCase):
    def test_merging_two_sorted_lists(self):
        self.assertEqual(merging_two_sorted_lists([5, 10, 15], [3, 8, 9]), [3, 5, 8, 9, 10, 15])
        self.assertEqual(merging_two_sorted_lists([5, 10, 15, 17], [3, 8, 9]), [3, 5, 8, 9, 10, 15, 17])
        self.assertEqual(merging_two_sorted_lists([5, 10, 15, 17], [3, 6, 8, 9]), [3, 5, 6, 8, 9, 10, 15, 17])
        self.assertEqual(merging_two_sorted_lists([5, 10, 15, 17, 21], [3, 7, 8, 9]), [3, 5, 7, 8, 9, 10, 15, 17, 21])
        self.assertEqual(merging_two_sorted_lists([5, 10, 15, 17], [3, 8, 9, 89]), [3, 5, 8, 9, 10, 15, 17, 89])

if __name__ == "__main__":
    unittest.main(verbosity=2)