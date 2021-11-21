import unittest

from palindrome_integer import palindrome_integer, palindrome_integer_string, palindrome_integer_integer

class TestCases(unittest.TestCase):
    def test_palindrome_integer(self):
        self.assertEqual(palindrome_integer(121), True)
        self.assertEqual(palindrome_integer(123), False)
        self.assertEqual(palindrome_integer(0), True)
        self.assertEqual(palindrome_integer(123454321), True)
        self.assertEqual(palindrome_integer(1234554321), True)
        self.assertEqual(palindrome_integer(123363456356), False)

    def test_palindrome_integer_string(self):
        self.assertEqual(palindrome_integer_string(121), True)
        self.assertEqual(palindrome_integer_string(123), False)
        self.assertEqual(palindrome_integer_string(0), True)
        self.assertEqual(palindrome_integer_string(123454321), True)
        self.assertEqual(palindrome_integer_string(1234554321), True)
        self.assertEqual(palindrome_integer_string(123363456356), False)

    def test_palindrome_integer_integer(self):
        self.assertEqual(palindrome_integer_integer(121), True)
        self.assertEqual(palindrome_integer_integer(123), False)
        self.assertEqual(palindrome_integer_integer(0), True)
        self.assertEqual(palindrome_integer_integer(123454321), True)
        self.assertEqual(palindrome_integer_integer(1234554321), True)
        self.assertEqual(palindrome_integer_integer(123363456356), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)