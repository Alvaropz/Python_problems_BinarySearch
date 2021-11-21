import unittest

from high_frequency import high_frequency

class TestCases(unittest.TestCase):
    def test_high_frequency(self):
        self.assertEqual(high_frequency([1, 4, 1, 7, 1, 7, 1, 1]), 5)
        self.assertEqual(high_frequency([5, 5, 5, 5, 5, 5, 5]), 7)
        self.assertEqual(high_frequency([1, 2, 3, 4, 5, 6, 7]), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)