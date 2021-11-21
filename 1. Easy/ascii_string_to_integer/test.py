import unittest

from ascii_string_to_integer import ascii_string_to_integer

class TestCases(unittest.TestCase):
    def test_ascii_string_to_integer(self):
        self.assertEqual(ascii_string_to_integer("11aa32bbb5"), 48)
        self.assertEqual(ascii_string_to_integer("1a2b3"), 6)
        self.assertEqual(ascii_string_to_integer("1135"), 1135)
        self.assertEqual(ascii_string_to_integer("abcd"), 0)
        self.assertEqual(ascii_string_to_integer("1a23b45c66defghijkl"), 135)

if __name__ == "__main__":
    unittest.main(verbosity=2)