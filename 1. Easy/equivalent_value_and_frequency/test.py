import unittest

from equivalent_value_and_frequency import equivalent_value_and_frequency

class TestCases(unittest.TestCase):
    def test_equivalent_value_and_frequency(self):
        self.assertEqual(equivalent_value_and_frequency([7, 9, 3, 3, 3]), True)
        self.assertEqual(equivalent_value_and_frequency([]), False)
        self.assertEqual(equivalent_value_and_frequency([7, 9, 3, 3]), False)
        self.assertEqual(equivalent_value_and_frequency([0]), False)
        self.assertEqual(equivalent_value_and_frequency([1]), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)