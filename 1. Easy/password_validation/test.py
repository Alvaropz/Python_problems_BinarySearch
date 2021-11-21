import unittest

from password_validation import password_validation

class TestCases(unittest.TestCase):
    def test_password_validation(self):
        self.assertEqual(password_validation("aA0@1234"), True)
        self.assertEqual(password_validation("B,84653?ab"), True)
        self.assertEqual(password_validation("aaaaAAAA1234"), False)
        self.assertEqual(password_validation("AAAA1234@"), False)
        self.assertEqual(password_validation("aaaa1234@"), False)
        self.assertEqual(password_validation("aaaaAAAA@"), False)
        self.assertEqual(password_validation("aA0@1234aA0@1234aA0@1234aA0@1234"), False)
        self.assertEqual(password_validation("a"), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)