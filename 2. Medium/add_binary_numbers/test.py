import unittest

from add_binary_numbers import add_binary_numbers

class TestCases(unittest.TestCase):
    def test_add_binary_numbers(self):
        self.assertEqual(add_binary_numbers("1", "1"), "10")
        self.assertEqual(add_binary_numbers("111", "10110101"), '10111100')
        self.assertEqual(add_binary_numbers("10101", "1011101"), '1110010')
        self.assertEqual(add_binary_numbers("10", "10"), '100')
        self.assertEqual(add_binary_numbers("101001000101", "1010111010101"), '10000000011010')
        self.assertEqual(add_binary_numbers("101", "10101011100101010101"), '10101011100101011010')

if __name__ == "__main__":
    unittest.main(verbosity=2)