import unittest

from compress_string import compress_string

class TestCases(unittest.TestCase):
    def test_compress_string(self):
        self.assertEqual(compress_string("aaaaaabbbccccaaaaddf"), "abcadf")
        self.assertEqual(compress_string("a"), "a")
        self.assertEqual(compress_string("eeeeeee"), "e")
        self.assertEqual(compress_string("uuuuuaaaaammmmmu"), "uamu")

if __name__ == "__main__":
    unittest.main(verbosity=2)