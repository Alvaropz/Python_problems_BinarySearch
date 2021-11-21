import unittest

from anagram_checks import anagram_checks

class TestCases(unittest.TestCase):
    def test_anagram_checks(self):
        self.assertEqual(anagram_checks("listen", "silent"), True)
        self.assertEqual(anagram_checks("bedroom", "bathroom"), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)