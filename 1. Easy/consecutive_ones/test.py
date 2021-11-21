import unittest

from consecutive_ones import consecutive_ones

class TestCases(unittest.TestCase):
    def test_consecutive_ones(self):
        self.assertEqual(consecutive_ones([0, 1, 1, 1, 2, 3]), True)
        self.assertEqual(consecutive_ones([1, 1, 1, 1, 1, 1]), True)
        self.assertEqual(consecutive_ones([1, 2, 1]), False)
        self.assertEqual(consecutive_ones([1]), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)