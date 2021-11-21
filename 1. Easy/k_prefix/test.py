import unittest

from k_prefix import k_prefix

class TestCases(unittest.TestCase):
    def test_k_prefix(self):
        self.assertEqual(k_prefix([3, -5, 4, 1, 6], 4), 3)
        self.assertEqual(k_prefix([-10, -3, -2, 12, 3], 4), 4)
        self.assertEqual(k_prefix([1], 0), -1)
        self.assertEqual(k_prefix([1, 2, 3, 4, 5, 6, 7], 3), 1)
        self.assertEqual(k_prefix([-10, 9, -8, 7, -6, 20, -4, 3, -1, 0], 8), 6)


if __name__ == "__main__":
    unittest.main(verbosity=2)