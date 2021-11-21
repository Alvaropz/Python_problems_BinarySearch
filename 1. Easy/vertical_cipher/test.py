import unittest

from vertical_cipher import vertical_cipher, vertical_cipher_optimised

class TestCases(unittest.TestCase):
    def test_vertical_cipher(self):
        self.assertEqual(vertical_cipher("abcdefghi", 5), ['af', 'bg', 'ch', 'di', 'e'])
        self.assertEqual(vertical_cipher("abcdefghi", 2), ['acegi', 'bdfh'])
        self.assertEqual(vertical_cipher("abcdefghi", 3), ['adg', 'beh', 'cfi'])
        self.assertEqual(vertical_cipher("abcdefghi", 1), ['abcdefghi'])
        self.assertEqual(vertical_cipher("", 1), [])

if __name__ == "__main__":
    unittest.main(verbosity=2)