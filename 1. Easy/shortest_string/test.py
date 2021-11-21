import unittest

from shortest_string import shortest_string

class TestCases(unittest.TestCase):
    def test_shortest_string(self):
        self.assertEqual(shortest_string("11000"), 1)
        self.assertEqual(shortest_string("1010"), 0)
        self.assertEqual(shortest_string("10100101"), 0)
        self.assertEqual(shortest_string("1"), 1)
        self.assertEqual(shortest_string("0"), 1)
        self.assertEqual(shortest_string("010110101010010101010101010111110101010101001001010"), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)