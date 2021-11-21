import unittest

from run_length_decoding import run_length_decoding

class TestCases(unittest.TestCase):
    def test_run_length_decoding(self):
        self.assertEqual(run_length_decoding("4a3b2c1d2a"), "aaaabbbccdaa")
        self.assertEqual(run_length_decoding("1a2b3c4d5e"), "abbcccddddeeeee")
        self.assertEqual(run_length_decoding("0a0b0c0d0e"), "")
        self.assertEqual(run_length_decoding("10a11b12c13d14e"), "aaaaaaaaaabbbbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeee")


if __name__ == "__main__":
    unittest.main(verbosity=2)