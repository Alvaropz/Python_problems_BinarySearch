import unittest

from inverse_factorial import inverse_factorial

class TestCases(unittest.TestCase):
    def test_inverse_factorial(self):
        self.assertEqual(inverse_factorial(1), 0)
        self.assertEqual(inverse_factorial(2), 2)
        self.assertEqual(inverse_factorial(3), -1)
        self.assertEqual(inverse_factorial(4), -1)
        self.assertEqual(inverse_factorial(5), -1)
        self.assertEqual(inverse_factorial(6), 3)
        self.assertEqual(inverse_factorial(7), -1)
        self.assertEqual(inverse_factorial(8), -1)
        self.assertEqual(inverse_factorial(9), -1)
        self.assertEqual(inverse_factorial(720), 6)
        self.assertEqual(inverse_factorial(17), -1)
        self.assertEqual(inverse_factorial(5040), 7)
        self.assertEqual(inverse_factorial(12312), -1)
        self.assertEqual(inverse_factorial(245634635), -1)
        self.assertEqual(inverse_factorial(245346736736), -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)