import unittest

from corner_diagonals import corner_diagonals

class TestCases(unittest.TestCase):
    def test_corner_diagonals(self):
        self.assertEqual(corner_diagonals(1),0)
        self.assertEqual(corner_diagonals(2), 0)
        self.assertEqual(corner_diagonals(3), 4)
        self.assertEqual(corner_diagonals(4), 8)
        self.assertEqual(corner_diagonals(5), 16)
        self.assertEqual(corner_diagonals(6), 24)
        self.assertEqual(corner_diagonals(7), 36)
        self.assertEqual(corner_diagonals(10), 80)


if __name__ == "__main__":
    unittest.main(verbosity=2)