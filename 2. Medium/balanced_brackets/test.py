import unittest

from balanced_brackets import balanced_brackets

class TestCases(unittest.TestCase):
    def test_balanced_brackets(self):
        self.assertEqual(balanced_brackets(")("), False)
        self.assertEqual(balanced_brackets("((()))"), True)
        self.assertEqual(balanced_brackets("()"), True)
        self.assertEqual(balanced_brackets("((()))"), True)
        self.assertEqual(balanced_brackets(""), True)
        self.assertEqual(balanced_brackets("((()"), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)