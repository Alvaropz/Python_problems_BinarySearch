import unittest

from string_sequence import string_sequence

class TestCases(unittest.TestCase):
    def test_string_sequence(self):
        self.assertEqual(string_sequence("a", "b", 4), "bbaba")
        self.assertEqual(string_sequence("ac", "bd", 7), "bdbdacbdbdacbdacbdbdacbdbdacbdacbdbdacbdac")
        self.assertEqual(string_sequence("e", "dc", 2), "dce")
        self.assertEqual(string_sequence("j", "g", 10), "ggjggjgjggjggjgjggjgjggjggjgjggjggjgjggjgjggjggjgjggjgjggjggjgjggjggjgjggjgjggjggjgjggjgj")

if __name__ == "__main__":
    unittest.main(verbosity=2)