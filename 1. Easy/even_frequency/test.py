import unittest

from even_frequency import even_frequency

class TestCases(unittest.TestCase):
    def test_even_frequency(self):
        self.assertEqual(even_frequency([2, 4, 4, 2, 3, 3]), True)
        self.assertEqual(even_frequency([1]), False)
        self.assertEqual(even_frequency([1, 1, 1, 1, 1, 1]), True)
        self.assertEqual(even_frequency([0, 0]), True)
        self.assertEqual(even_frequency([1, 1, 2, 2, 5, 5, 5, 5]), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)