import unittest

from largest_anagram_group import largest_anagram_group

class TestCases(unittest.TestCase):
    def test_largest_anagram_group(self):
        self.assertEqual(largest_anagram_group(["ab", "ba", "abc", "cba", "bca", "ddddd"]), 3)
        self.assertEqual(largest_anagram_group(["a", "b"]), 1)
        self.assertEqual(largest_anagram_group(["aa", "bb"]), 1)
        self.assertEqual(largest_anagram_group(["abc"]), 1)
        self.assertEqual(largest_anagram_group(["abc", "bca", "acb", "dabc", "abcd", "bcda", "cdab"]), 4)

if __name__ == "__main__":
    unittest.main(verbosity=2)