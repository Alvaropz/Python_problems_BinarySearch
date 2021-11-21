import unittest

from largest_number_by_two_times import largest_number_by_two_times

class TestCases(unittest.TestCase):
    def test_largest_number_by_two_times(self):
        self.assertEqual(largest_number_by_two_times([3, 6, 9]), False)
        self.assertEqual(largest_number_by_two_times([3, 6, 15]), True)
        self.assertEqual(largest_number_by_two_times([3, 6, 12]), False)
        self.assertEqual(largest_number_by_two_times([3, 1]), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)