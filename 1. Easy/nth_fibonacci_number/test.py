import unittest

from nth_fibonacci_number import fibonacci

class TestCases(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(15), 610)
        self.assertEqual(fibonacci(3), 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)