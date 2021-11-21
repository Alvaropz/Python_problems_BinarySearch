import unittest

from longest_consecutive_duplicate_string import longest_consecutive_duplicate_string

class TestCases(unittest.TestCase):
    def test_longest_consecutive_duplicate_string(self):
        self.assertEqual(longest_consecutive_duplicate_string("abbbba"), 4)
        self.assertEqual(longest_consecutive_duplicate_string(""), 0)
        self.assertEqual(longest_consecutive_duplicate_string("ab"), 0)
        self.assertEqual(longest_consecutive_duplicate_string("aaaabbbb"), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)