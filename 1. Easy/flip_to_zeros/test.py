import unittest

from flip_to_zeros import flip_to_zeros

class TestCases(unittest.TestCase):
    def test_flip_to_zeros(self):
        self.assertEqual(flip_to_zeros([]), 0)
        self.assertEqual(flip_to_zeros([0]), 0)
        self.assertEqual(flip_to_zeros([1]), 1)
        self.assertEqual(flip_to_zeros([0, 1]), 1)
        self.assertEqual(flip_to_zeros([1, 0]), 2)
        self.assertEqual(flip_to_zeros([0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1]), 13)
        self.assertEqual(flip_to_zeros([1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1]), 15)

if __name__ == "__main__":
    unittest.main(verbosity=2)