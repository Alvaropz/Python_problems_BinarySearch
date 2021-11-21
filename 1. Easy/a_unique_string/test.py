import unittest

from a_unique_string import a_unique_string, a_unique_string_optimised

class TestCases(unittest.TestCase):
    def test_a_unique_string(self):
        self.assertEqual(a_unique_string("a"), True)
        self.assertEqual(a_unique_string("ab"), True)
        self.assertEqual(a_unique_string("abc"), True)
        self.assertEqual(a_unique_string("abcda"), False)
        self.assertEqual(a_unique_string("abcdee"), False)
        self.assertEqual(a_unique_string(""), True)
    
    
    def test_a_unique_string_optimised(self):
        self.assertEqual(a_unique_string_optimised("a"), True)
        self.assertEqual(a_unique_string_optimised("ab"), True)
        self.assertEqual(a_unique_string_optimised("abc"), True)
        self.assertEqual(a_unique_string_optimised("abcda"), False)
        self.assertEqual(a_unique_string_optimised("abcdee"), False)
        self.assertEqual(a_unique_string_optimised(""), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)