import unittest

from string_clockwise_shift import string_clockwise_shift

class TestCases(unittest.TestCase):
    def test_string_clockwise_shift(self):
        self.assertEqual(string_clockwise_shift("xyz", "zzz", 3), True)
        self.assertEqual(string_clockwise_shift("zzz", "zzz", 0), True)
        self.assertEqual(string_clockwise_shift("aa", "zz", 3), False)
        self.assertEqual(string_clockwise_shift("aa", "zz", 4), False)
        self.assertEqual(string_clockwise_shift("zz", "aa", 3), True)
        self.assertEqual(string_clockwise_shift("aa", "zz", 50), True)
        self.assertEqual(string_clockwise_shift("aa", "zz", 49), False)
        self.assertEqual(string_clockwise_shift("aacea", "xbhasd", 100), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)