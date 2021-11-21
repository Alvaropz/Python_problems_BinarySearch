import unittest

from strictly_increasing_or_strictly_decreasing import strictly_increasing_or_strictly_decreasing

class TestCases(unittest.TestCase):
    def test_strictly_increasing_or_strictly_decreasing(self):
        self.assertEqual(strictly_increasing_or_strictly_decreasing([1, 2, 3, 4, 5]), True)
        self.assertEqual(strictly_increasing_or_strictly_decreasing([1, 2, 3, 4, 5, 5]), False)
        self.assertEqual(strictly_increasing_or_strictly_decreasing([5, 4, 3, 2, 1]), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)