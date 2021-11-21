import unittest

from narcissistic_number import narcissistic_number

class TestCases(unittest.TestCase):
    def test_narcissistic_number(self):
        self.assertEqual(narcissistic_number(153), True)
        self.assertEqual(narcissistic_number(1), True)
        self.assertEqual(narcissistic_number(55), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)