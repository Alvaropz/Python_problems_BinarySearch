import unittest

from repeated_addition import repeated_addition

class TestCases(unittest.TestCase):
    def test_repeated_addition(self):
        self.assertEqual(repeated_addition(3456), 9)
        self.assertEqual(repeated_addition(11), 2)
        self.assertEqual(repeated_addition(5), 5)
        self.assertEqual(repeated_addition(888888), 3)

if __name__ == "__main__":
    unittest.main(verbosity=2)