import unittest

from run_length_encoding import run_length_encoding_string, run_length_encoding_list

class TestCases(unittest.TestCase):
    def test_run_length_encoding_string(self):
        self.assertEqual(run_length_encoding_string("AAAABBBCCDAA"), '4A3B2C1D2A')
        self.assertEqual(run_length_encoding_string("ABCDE"), '1A1B1C1D1E')

    def test_run_length_encoding_list(self):
        self.assertEqual(run_length_encoding_list("AAAABBBCCDAA"), '4A3B2C1D2A')
        self.assertEqual(run_length_encoding_list("ABCDE"), '1A1B1C1D1E')


if __name__ == "__main__":
    unittest.main(verbosity=2)