import unittest

from longest_consecutive_run_of_ones_in_binary import longest_consecutive_run_of_ones_in_binary

class TestCases(unittest.TestCase):
    def test_longest_consecutive_run_of_ones_in_binary(self):
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(1), 1)
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(2), 1)
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(3), 2)
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(4), 1)
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(5), 1)
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(6), 2)
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(7), 3)
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(8), 1)
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(9), 1)
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(11), 2)
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(123), 4)
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(156), 3)
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(189), 4)
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(1259), 3)
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(12591), 4)
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(125914), 4)
        self.assertEqual(longest_consecutive_run_of_ones_in_binary(1259146), 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)