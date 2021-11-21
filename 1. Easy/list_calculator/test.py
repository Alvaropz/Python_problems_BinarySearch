import unittest

from list_calculator import operations

class TestCases(unittest.TestCase):
    def test_operations(self):
        self.assertEqual(operations([3, 1, 6], "+", 4), [7, 5, 10])
        self.assertEqual(operations([3, 1, 6], "-", 4), [-1, -3, 2])
        self.assertEqual(operations([3, 1, 6], "*", 4), [12, 4, 24])
        self.assertEqual(operations([3, 1, 6], "/", 4), [0, 0, 1])


if __name__ == "__main__":
    unittest.main(verbosity=2)