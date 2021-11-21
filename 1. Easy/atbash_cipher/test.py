import unittest

from atbash_cipher import atbash_cipher_ascii_index, atbash_cipher_alphabet_lists_iteration, atbash_cipher_lists_accesing_index

class TestCases(unittest.TestCase):
    def test_atbash_cipher_ascii_index(self):
        self.assertEqual(atbash_cipher_ascii_index("abcdefghijklmnopqrstuvwxyz"), "zyxwvutsrqponmlkjihgfedcba")
    
    def test_atbash_cipher_alphabet_lists_iteration(self):
        self.assertEqual(atbash_cipher_alphabet_lists_iteration("abcdefghijklmnopqrstuvwxyz"), "zyxwvutsrqponmlkjihgfedcba")

    def test_atbash_cipher_lists_accesing_index(self):
        self.assertEqual(atbash_cipher_lists_accesing_index("abcdefghijklmnopqrstuvwxyz"), "zyxwvutsrqponmlkjihgfedcba")


if __name__ == "__main__":
    unittest.main(verbosity=2)