import unittest

from mixed_sorting import mixed_sorting

class TestCases(unittest.TestCase):
    def test_mixed_sorting(self):
        self.assertEqual(mixed_sorting([8, 13, 11, 90, -5, 4]), [4, 13, 11, 8, -5, 90])
        self.assertEqual(mixed_sorting([1, 2, 3, 4, 5]), [5, 2, 3, 4, 1])
        self.assertEqual(mixed_sorting([1, 3, 5, 7, 9]), [9, 7, 5, 3, 1])
        self.assertEqual(mixed_sorting([2, 4, 6, 8, 10]), [2, 4, 6, 8, 10])
        self.assertEqual(mixed_sorting([-7, 5, -5, 1, 2, -15, 3, 0, 4, 65]), [65, 5, 3, 1, 0, -5, -7, 2, 4, -15])

if __name__ == "__main__":
    unittest.main(verbosity=2)