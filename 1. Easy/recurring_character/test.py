import unittest

from recurring_character import recurring_character

class TestCases(unittest.TestCase):
    def test_recurring_character(self):
        self.assertEqual(recurring_character("abcda"), 4)
        self.assertEqual(recurring_character("aaaaa"), 1)
        self.assertEqual(recurring_character("abcde"), -1)
        self.assertEqual(recurring_character("abcdee"), 5)
        self.assertEqual(recurring_character("v"), -1)

if __name__ == "__main__":
    unittest.main(verbosity=2)