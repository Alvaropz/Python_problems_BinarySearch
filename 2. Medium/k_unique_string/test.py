import unittest

from k_unique_string import k_unique_string

class TestCases(unittest.TestCase):
    def test_k_unique_string(self):
        self.assertEqual(k_unique_string("daabbccaajh", 4), 2)
        self.assertEqual(k_unique_string("daabbccaajh", 0), 11)
        self.assertEqual(k_unique_string("daabbccaa", 2), 3)
        self.assertEqual(k_unique_string("daabbccaajksbdak", 3), 6)
        self.assertEqual(k_unique_string("ab", 1), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)