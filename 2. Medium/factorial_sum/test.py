import unittest

from factorial_sum import factorial_sum

class TestCases(unittest.TestCase):
    def test_factorial_sum(self):
        self.assertEqual(factorial_sum(1), True)
        self.assertEqual(factorial_sum(2), True)
        self.assertEqual(factorial_sum(6), True)
        self.assertEqual(factorial_sum(7), True)
        self.assertEqual(factorial_sum(11), False)
        self.assertEqual(factorial_sum(26), True)
        self.assertEqual(factorial_sum(29), False)
        self.assertEqual(factorial_sum(31), True)
        self.assertEqual(factorial_sum(100), False)
        self.assertEqual(factorial_sum(500), False)
        self.assertEqual(factorial_sum(720), True)
        self.assertEqual(factorial_sum(726), True)
        self.assertEqual(factorial_sum(741), False)
        self.assertEqual(factorial_sum(841), True)
        self.assertEqual(factorial_sum(362881), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)