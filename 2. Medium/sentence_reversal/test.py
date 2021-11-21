import unittest

from sentence_reversal import sentence_reversal_optimised, sentence_reversal

class TestCases(unittest.TestCase):
    def test_sentence_reversal_optimised(self):
        self.assertEqual(sentence_reversal_optimised(["h","i"," ","w","o","r","l","d"]), ['w', 'o', 'r', 'l', 'd', ' ', 'h', 'i'])
        self.assertEqual(sentence_reversal_optimised(["w","o","r","l","d"]), ['w', 'o', 'r', 'l', 'd'])
        self.assertEqual(sentence_reversal_optimised(["h","i"," ","w","o","r","l","d", " ", "g", "o", "o", "d", " ", "m", "o", "r", "n", "i", "n", "g"]), ["m", "o", "r", "n", "i", "n", "g", " ", "g", "o", "o", "d", " ", 'w', 'o', 'r', 'l', 'd', ' ', 'h', 'i'])

    def test_sentence_reversal(self):
        self.assertEqual(sentence_reversal(["h","i"," ","w","o","r","l","d"]), ['w', 'o', 'r', 'l', 'd', ' ', 'h', 'i'])
        self.assertEqual(sentence_reversal(["w","o","r","l","d"]), ['w', 'o', 'r', 'l', 'd'])
        self.assertEqual(sentence_reversal(["h","i"," ","w","o","r","l","d", " ", "g", "o", "o", "d", " ", "m", "o", "r", "n", "i", "n", "g"]), ["m", "o", "r", "n", "i", "n", "g", " ", "g", "o", "o", "d", " ", 'w', 'o', 'r', 'l', 'd', ' ', 'h', 'i'])

if __name__ == "__main__":
    unittest.main(verbosity=2)