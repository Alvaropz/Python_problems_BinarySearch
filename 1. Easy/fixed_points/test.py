import unittest

from fixed_points import fixed_points

class TestCases(unittest.TestCase):
    def test_fixed_points(self):
        self.assertEqual(fixed_points([-5, -2, 0, 3, 4]), 3)
        self.assertEqual(fixed_points([0]), 0)
        self.assertEqual(fixed_points([-1, -2, -3, -4, 0, 5]), 5)
        self.assertEqual(fixed_points([-1, -2, -3, -4]), -1)
        self.assertEqual(fixed_points([]), -1)

if __name__ == "__main__":
    unittest.main(verbosity=2)