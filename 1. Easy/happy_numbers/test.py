import unittest

from happy_numbers import happy_numbers

class TestCases(unittest.TestCase):
    def test_happy_numbers(self):
        self.assertEqual(happy_numbers(7), True)
        self.assertEqual(happy_numbers(0), False)
        self.assertEqual(happy_numbers(1), True)
        self.assertEqual(happy_numbers(5), False)
        self.assertEqual(happy_numbers(11), False)
        self.assertEqual(happy_numbers(70), True)
        self.assertEqual(happy_numbers(71), False)
        self.assertEqual(happy_numbers(79), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)