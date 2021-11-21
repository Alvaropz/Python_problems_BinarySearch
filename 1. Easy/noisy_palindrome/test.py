import unittest

from noisy_palindrome import noisy_palindrome

class TestCases(unittest.TestCase):
    def test_noisy_palindrome(self):
        self.assertEqual(noisy_palindrome("a92bcbXa"), True)
        self.assertEqual(noisy_palindrome("a92bcbXA"), False)
        self.assertEqual(noisy_palindrome("a92bcbXa12"), True)
        self.assertEqual(noisy_palindrome("a92bcbXa1a"), False)
        self.assertEqual(noisy_palindrome("abcba"), True)
        self.assertEqual(noisy_palindrome("1a2b3c4b5a6"), True)
        self.assertEqual(noisy_palindrome("1a2b3c4b5a6XBVHAJDKW"), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)