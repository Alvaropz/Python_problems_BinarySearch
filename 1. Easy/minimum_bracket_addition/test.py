import unittest

from minimum_bracket_addition import minimum_bracket_addition

class TestCases(unittest.TestCase):
    def test_minimum_bracket_addition(self):
        self.assertEqual(minimum_bracket_addition(")))(("), 5)
        self.assertEqual(minimum_bracket_addition(")))(())"), 3)
        self.assertEqual(minimum_bracket_addition("()"), 0)
        self.assertEqual(minimum_bracket_addition("(()))())(("), 4)
        self.assertEqual(minimum_bracket_addition("((()))"), 0)
        self.assertEqual(minimum_bracket_addition("(()((())(((()))"), 3)

if __name__ == "__main__":
    unittest.main(verbosity=2)