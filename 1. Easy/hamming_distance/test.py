import unittest

from hamming_distance import hamming_distance

class TestCases(unittest.TestCase):
    def test_hamming_distance(self):
        self.assertEqual(hamming_distance(9, 5), 2)
        self.assertEqual(hamming_distance(1, 1), 0)
        self.assertEqual(hamming_distance(12, 1), 3)
        self.assertEqual(hamming_distance(5, 3), 2)
        self.assertEqual(hamming_distance(3, 5), 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)