import unittest

from CCCXXVV import CCCXXVV

class TestCases(unittest.TestCase):
    def test_CCCXXVV(self):
        self.assertEqual(CCCXXVV("XIV"), 14)
        self.assertEqual(CCCXXVV("MCDXCII"), 1492)
        self.assertEqual(CCCXXVV("MMLXXVII"), 2077)
        self.assertEqual(CCCXXVV("I"), 1)
        self.assertEqual(CCCXXVV("III"), 3)
        self.assertEqual(CCCXXVV("XCIX"), 99)
        self.assertEqual(CCCXXVV("MCMXLIV"), 1944)
        self.assertEqual(CCCXXVV("XVIII"), 18)
        self.assertEqual(CCCXXVV(""), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)