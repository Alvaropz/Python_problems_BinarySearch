import unittest

from repeated_k_length_substrings import repeated_k_length_substrings, repeated_k_length_substrings_optimised

class TestCases(unittest.TestCase):
    def test_repeated_k_length_substrings(self):
        self.assertEqual(repeated_k_length_substrings("abcdabc", 3), 1)
        self.assertEqual(repeated_k_length_substrings("aaabbb", 2), 2)
        self.assertEqual(repeated_k_length_substrings("aaaaaa", 1), 1)
        self.assertEqual(repeated_k_length_substrings("abcdefg", 2), 0)

    def test_repeated_k_length_substrings_optimised(self):
        self.assertEqual(repeated_k_length_substrings_optimised("abcdabc", 3), 1)
        self.assertEqual(repeated_k_length_substrings_optimised("aaabbb", 2), 2)
        self.assertEqual(repeated_k_length_substrings_optimised("aaaaaa", 1), 1)
        self.assertEqual(repeated_k_length_substrings_optimised("abcdefg", 2), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)