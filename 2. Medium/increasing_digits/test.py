import unittest

from increasing_digits import increasing_digits

class TestCases(unittest.TestCase):
    def test_increasing_digits(self):
        self.assertEqual(increasing_digits(1), 9)
        self.assertEqual(increasing_digits(2), 36)
        self.assertEqual(increasing_digits(3), 84)
        self.assertEqual(increasing_digits(4), 126)
        self.assertEqual(increasing_digits(5), 126)
        self.assertEqual(increasing_digits(6), 84)
        self.assertEqual(increasing_digits(7), 36)
        self.assertEqual(increasing_digits(8), 9)
        self.assertEqual(increasing_digits(9), 1)
        self.assertEqual(increasing_digits(10), 0)
        self.assertEqual(increasing_digits(11), 0)
        self.assertEqual(increasing_digits(12), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)