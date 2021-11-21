import unittest

from reverse_sentence import reverse_sentence

class TestCases(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_sentence("hello there my friend"), "friend my there hello")
        self.assertEqual(reverse_sentence("It's a wonderful day for pie"), "pie for day wonderful a It's")
        self.assertEqual(reverse_sentence("Blue"), "Blue")
        self.assertEqual(reverse_sentence("Bear the Bear"), "Bear the Bear")

if __name__ == "__main__":
    unittest.main(verbosity=2)