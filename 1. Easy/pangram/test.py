import unittest

from pangram import pangram, pangram_v2, pangram_v3

class TestCases(unittest.TestCase):
    def test_pangram(self):
        self.assertEqual(pangram("A quick brown fox jumps over the lazy dog"), True)
        self.assertEqual(pangram("The jay, pig, fox, tiger and my wolves quack!"), False)
        self.assertEqual(pangram("This is very convinient!"), False)
        self.assertEqual(pangram("AbCdEfGhIjKlMnOpQrStUvWxYz! That's the alphabet in English!"), True)

    def test_pangram_v2(self):
        self.assertEqual(pangram_v2("A quick brown fox jumps over the lazy dog"), True)
        self.assertEqual(pangram_v2("The jay, pig, fox, tiger and my wolves quack!"), False)
        self.assertEqual(pangram_v2("This is very convinient!"), False)
        self.assertEqual(pangram_v2("AbCdEfGhIjKlMnOpQrStUvWxYz! That's the alphabet in English!"), True)

    def test_pangram_v3(self):
        self.assertEqual(pangram_v3("A quick brown fox jumps over the lazy dog"), True)
        self.assertEqual(pangram_v3("The jay, pig, fox, tiger and my wolves quack!"), False)
        self.assertEqual(pangram_v3("This is very convinient!"), False)
        self.assertEqual(pangram_v3("AbCdEfGhIjKlMnOpQrStUvWxYz! That's the alphabet in English!"), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)