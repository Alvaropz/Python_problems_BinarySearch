import unittest

from pascals_triangle import pascals_triangle

class TestCases(unittest.TestCase):
    def test_pascals_triangle(self):
        self.assertEqual(pascals_triangle(0), [1])
        self.assertEqual(pascals_triangle(1), [1, 1])
        self.assertEqual(pascals_triangle(2), [1, 2, 1])
        self.assertEqual(pascals_triangle(3), [1, 3, 3, 1])
        self.assertEqual(pascals_triangle(4), [1, 4, 6, 4, 1])
        self.assertEqual(pascals_triangle(5), [1, 5, 10, 10, 5, 1])
        self.assertEqual(pascals_triangle(6), [1, 6, 15, 20, 15, 6, 1])
        self.assertEqual(pascals_triangle(7), [1, 7, 21, 35, 35, 21, 7, 1])
        self.assertEqual(pascals_triangle(8), [1, 8, 28, 56, 70, 56, 28, 8, 1])
        self.assertEqual(pascals_triangle(9), [1, 9, 36, 84, 126, 126, 84, 36, 9, 1])
        self.assertEqual(pascals_triangle(10),[1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1])

if __name__ == "__main__":
    unittest.main(verbosity=2)