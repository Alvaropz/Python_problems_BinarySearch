import unittest

from parentheses_grouping import parentheses_grouping

class TestCases(unittest.TestCase):
    def test_parentheses_grouping(self):
        self.assertEqual(parentheses_grouping("()()(()())"), ['()', '()', '(()())'])
        self.assertEqual(parentheses_grouping("()()"), ['()', '()'])
        self.assertEqual(parentheses_grouping("(()())"), ['(()())'])
        self.assertEqual(parentheses_grouping("((()))(())()()(((())))"), ['((()))', '(())', '()', '()', '(((())))'])
        self.assertEqual(parentheses_grouping("()"), ['()'])


if __name__ == "__main__":
    unittest.main(verbosity=2)