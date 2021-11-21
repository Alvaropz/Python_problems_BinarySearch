import unittest

from palindrome_count import palindrome_count_dict, palindrome_count_set

class TestCases(unittest.TestCase):
    def test_palindrome_count_dict(self):
        self.assertEqual(palindrome_count_dict("ab", 4), 4) # ["aaaa", "bbbb", "abba", "baab"]
        self.assertEqual(palindrome_count_dict("abcd", 4), 16)
        self.assertEqual(palindrome_count_dict("abcd", 12), 4096)
        self.assertEqual(palindrome_count_dict("abcde", 1), 5)
        self.assertEqual(palindrome_count_dict("abbbbcde", 7), 625)

    def test_palindrome_count_set(self):
        self.assertEqual(palindrome_count_set("ab", 4), 4) # ["aaaa", "bbbb", "abba", "baab"]
        self.assertEqual(palindrome_count_set("abcd", 4), 16)
        self.assertEqual(palindrome_count_set("abcd", 12), 4096)
        self.assertEqual(palindrome_count_set("abcde", 1), 5)
        self.assertEqual(palindrome_count_set("abbbbcde", 7), 625)


if __name__ == "__main__":
    unittest.main(verbosity=2)