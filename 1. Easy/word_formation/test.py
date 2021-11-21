import unittest

from word_formation import word_formation

class TestCases(unittest.TestCase):
    def test_word_formation(self):
        self.assertEqual(word_formation(["the", "word", "love", "scott", "finder", "dictionary"], "fanierdow"), 6)
        self.assertEqual(word_formation(["juniper", "aaa"], "afnvlafkma"), 3)
        self.assertEqual(word_formation(["credit", "nirvana", "karma", "empathy", "hang", "aaaaaaaaa"], "afnvlfkm"), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)