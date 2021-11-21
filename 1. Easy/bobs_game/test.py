import unittest

from bobs_game import bobs_game

class TestCases(unittest.TestCase):
    def test_bobs_game(self):
        self.assertEqual(bobs_game([1, 1, 3, 7, 6, 12]), 2)
        self.assertEqual(bobs_game([1, 1]), 1)
        self.assertEqual(bobs_game([1, 2]), -1)
        self.assertEqual(bobs_game([2, 2]), 0)
        self.assertEqual(bobs_game([1, 1, 3, 7, 9, 11]), 3)
        self.assertEqual(bobs_game([2, 4, 6, 8, 10, 12]), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)