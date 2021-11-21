import unittest

from equivalent_pairs import equivalent_pairs

class TestCases(unittest.TestCase):
    def test_equivalent_pairs(self):
        self.assertEqual(equivalent_pairs([7, 1, 4, 3, 2, 5, 3, 7, 2, 6, 5, 4, 1, 9, 4, 8, 1, 3, 9, 3]), 16)
        self.assertEqual(equivalent_pairs([2, 6, 8, 3, 2, 8, 9, 1, 8, 4, 4, 6, 6, 3, 4, 4, 1, 7, 7, 8]), 19)
        self.assertEqual(equivalent_pairs([3, 1, 3, 3, 3, 2, 3, 2, 2, 2, 3, 2, 1, 3, 3, 1, 2, 4, 2, 1]), 55)
        self.assertEqual(equivalent_pairs([1, 9, 13, 6, 8, 13, 15, 18, 18, 17, 8, 6, 4, 13, 14, 16, 19, 2, 17, 16]), 8)
        self.assertEqual(equivalent_pairs([3, 14, 19, 10, 8, 15, 6, 3, 9, 10, 12, 5, 10, 8, 18, 15, 10, 6, 1, 4]), 10)
        self.assertEqual(equivalent_pairs([1, 12, 10, 8, 6, 8, 3, 18, 19, 18, 2, 9, 12, 13, 16, 19, 2, 9, 7, 16]), 7)
        self.assertEqual(equivalent_pairs([3,2,3,2,1,2,4,7,5,5,1,2,2,4,8,1,7,3]), 19)
        self.assertEqual(equivalent_pairs([3,2,3,2,2]), 4)

if __name__ == "__main__":
    unittest.main(verbosity=2)