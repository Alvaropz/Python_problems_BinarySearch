import unittest

from vigenere_cipher import vigenere_cipher, vigenere_cipher_zip

class TestCases(unittest.TestCase):
    def test_vigenere_cipher(self):
        self.assertEqual(vigenere_cipher("bcd", "bbb"), "cde")
        self.assertEqual(vigenere_cipher("abc", "cde"), "ceg")
        self.assertEqual(vigenere_cipher("xyz", "bbb"), "yza")
        self.assertEqual(vigenere_cipher("fgjq", "jiag"), "oojw")

    def test_vigenere_cipher_zip(self):
        self.assertEqual(vigenere_cipher_zip("bcd", "bbb"), "cde")
        self.assertEqual(vigenere_cipher_zip("abc", "cde"), "ceg")
        self.assertEqual(vigenere_cipher_zip("xyz", "bbb"), "yza")
        self.assertEqual(vigenere_cipher_zip("fgjq", "jiag"), "oojw")



if __name__ == "__main__":
    unittest.main(verbosity=2)