import unittest

from palindromic_anagram import palindromic_anagram

class TestCases(unittest.TestCase):
    def test_palindromic_anagram(self):
        self.assertEqual(palindromic_anagram("carrace"), True)
        self.assertEqual(palindromic_anagram("bbbzizzz"), False)
        self.assertEqual(palindromic_anagram("caacjb"), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)