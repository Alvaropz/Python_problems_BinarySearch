import unittest

from factorial_factory import factorial_factory

class TestCases(unittest.TestCase):
    def test_factorial_factory(self):
        self.assertEqual(factorial_factory(1), 1)
        self.assertEqual(factorial_factory(2), 2)
        self.assertEqual(factorial_factory(3), 6)
        self.assertEqual(factorial_factory(4), 24)
        self.assertEqual(factorial_factory(5), 120)
        self.assertEqual(factorial_factory(6), 720)
        self.assertEqual(factorial_factory(7), 5040)
        self.assertEqual(factorial_factory(8), 40320)
        self.assertEqual(factorial_factory(9), 362880)
        self.assertEqual(factorial_factory(10),  3628800)

if __name__ == "__main__":
    unittest.main(verbosity=2)