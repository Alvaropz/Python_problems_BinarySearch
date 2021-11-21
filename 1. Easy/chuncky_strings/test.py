import unittest

from chuncky_strings import chuncky_strings_optimised, chuncky_strings

class TestCases(unittest.TestCase):

    def test_chuncky_strings_optimised(self):
        self.assertEqual(chuncky_strings_optimised("abcdefg", 3), ["abc", "def", "g"])
        self.assertEqual(chuncky_strings_optimised("abcdef", 2), ["ab", "cd", "ef"])
        self.assertEqual(chuncky_strings_optimised("", 3), [])

    def test_chuncky_strings(self):
        self.assertEqual(chuncky_strings("abcdefg", 3), ["abc", "def", "g"])
        self.assertEqual(chuncky_strings("abcdef", 2), ["ab", "cd", "ef"])
        self.assertEqual(chuncky_strings("", 3), [])
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
    