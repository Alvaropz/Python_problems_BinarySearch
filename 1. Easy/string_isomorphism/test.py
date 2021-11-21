import unittest

from string_isomorphism import string_isomorphism

class TestCases(unittest.TestCase):
    def test_string_isomorphism(self):
        self.assertEqual(string_isomorphism("coco", "kaka"), True)
        self.assertEqual(string_isomorphism("car", "foo"), False)
        self.assertEqual(string_isomorphism("miau", "guau"), False)
        self.assertEqual(string_isomorphism("extended", "abcadaaa"), False)
        self.assertEqual(string_isomorphism("abcadaaa", "extended"), False)
        self.assertEqual(string_isomorphism("extended", "abcadeae"), True)
        self.assertEqual(string_isomorphism("abcadeae", "extended"), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)