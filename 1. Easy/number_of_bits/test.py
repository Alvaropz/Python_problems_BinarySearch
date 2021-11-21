import unittest

from number_of_bits import number_of_bits

class TestCases(unittest.TestCase):
    def test_number_of_bits(self):
        self.assertEqual(number_of_bits(0), 0)
        self.assertEqual(number_of_bits(1), 1)
        self.assertEqual(number_of_bits(2), 1)
        self.assertEqual(number_of_bits(5), 2)
        self.assertEqual(number_of_bits(10), 2)
        self.assertEqual(number_of_bits(500), 6)
        self.assertEqual(number_of_bits(99999), 10)


if __name__ == "__main__":
    unittest.main(verbosity=2)