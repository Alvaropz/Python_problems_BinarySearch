import unittest

from beer_bottles import beer_bottles

class TestCases(unittest.TestCase):
    def test_beer_bottles(self):
        self.assertEqual(beer_bottles(3), 4)
        self.assertEqual(beer_bottles(6), 8)
        self.assertEqual(beer_bottles(9), 13)
        self.assertEqual(beer_bottles(12), 17)
        self.assertEqual(beer_bottles(15), 22)
        self.assertEqual(beer_bottles(18), 26)
        self.assertEqual(beer_bottles(21), 31)

if __name__ == "__main__":
    unittest.main(verbosity=2)