import unittest

from swap_consecutive_index_pairs import swap_consecutive_index_pairs

class TestCases(unittest.TestCase):
    def test_swap_consecutive_index_pairs(self):
        self.assertEqual(swap_consecutive_index_pairs([0, 1, 2, 3, 4, 5, 6, 7, 8]), [2, 3, 0, 1, 6, 7, 4, 5, 8])
        self.assertEqual(swap_consecutive_index_pairs([]), [])
        self.assertEqual(swap_consecutive_index_pairs([0, 1, 2]), [2, 1, 0])
        self.assertEqual(swap_consecutive_index_pairs([0, 2, 2]), [2, 2, 0])
        self.assertEqual(swap_consecutive_index_pairs([1]), [1])
        self.assertEqual(swap_consecutive_index_pairs([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [2, 3, 0, 1, 6, 7, 4, 5, 8, 9])

if __name__ == "__main__":
    unittest.main(verbosity=2)