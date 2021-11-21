import unittest

from target_number_with_operations import target_number_with_operations

class TestCases(unittest.TestCase):
    def test_target_number_with_operations(self):
        self.assertEqual(target_number_with_operations(0, 3), 3)
        self.assertEqual(target_number_with_operations(2, 9), 3)
        self.assertEqual(target_number_with_operations(3, 15), 4)
        self.assertEqual(target_number_with_operations(456, 2578), 191)
        self.assertEqual(target_number_with_operations(499999997, 1000000001), 5)

if __name__ == "__main__":
    unittest.main(verbosity=2)