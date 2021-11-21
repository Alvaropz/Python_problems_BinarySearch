import unittest

from minimum_string import minimum_string

class TestCases(unittest.TestCase):
    def test_minimum_string(self):
        self.assertEqual(minimum_string("ehyoe", "hello"), 2)
        self.assertEqual(minimum_string("jje", "jjj"), 1)
        self.assertEqual(minimum_string("ehyoe", "trees"), 3)
        self.assertEqual(minimum_string("col", "car"), 2)
        self.assertEqual(minimum_string("abbcccddddeeeeeffffff", "abcdef"), 15)

if __name__ == "__main__":
    unittest.main(verbosity=2)