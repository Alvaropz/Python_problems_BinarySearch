import unittest

from string_addition import string_addition

class TestCases(unittest.TestCase):
    def test_string_addition(self):
        self.assertEqual(string_addition("12", "23"), "35")
        self.assertEqual(string_addition("1", "1"), "2")
        self.assertEqual(string_addition("0", "0"), "0")
        self.assertEqual(string_addition("-15", "5"), "-10")

if __name__ == "__main__":
    unittest.main(verbosity=2)