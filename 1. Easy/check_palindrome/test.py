import unittest

from check_palindrome import check_palindrome_optimised, check_palindrome_slow

class TestCases(unittest.TestCase):
    def test_palindrome_optimised(self):
        self.assertEqual(check_palindrome_optimised("racecar"), True)
        self.assertEqual(check_palindrome_optimised("evilolive"), True)
        self.assertEqual(check_palindrome_optimised("si"), False)
        self.assertEqual(check_palindrome_optimised("no"), False)
        self.assertEqual(check_palindrome_optimised("laninaremilgadaesunadespechada"), False)

    def test_palindrome_slow(self):
        self.assertEqual(check_palindrome_slow("racecar"), True)
        self.assertEqual(check_palindrome_slow("evilolive"), True)
        self.assertEqual(check_palindrome_slow("si"), False)
        self.assertEqual(check_palindrome_slow("no"), False)
        self.assertEqual(check_palindrome_slow("laninaremilgadaesunadespechada"), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)