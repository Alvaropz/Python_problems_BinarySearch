import unittest

from counting_plus_plus import counting_plus_plus, counting_plus_plus_optimised

class TestCases(unittest.TestCase):
    def test_counting_plus_plus(self):
        self.assertEqual(counting_plus_plus([1, 2, 2, 3, 7]), 3)
        self.assertEqual(counting_plus_plus([1, 1]), 0)
        self.assertEqual(counting_plus_plus([1, 5, 7, 8]), 1)

    def test_counting_plus_plus_optimised(self):
        self.assertEqual(counting_plus_plus_optimised([1, 2, 2, 3, 7]), 3)
        self.assertEqual(counting_plus_plus_optimised([1, 1]), 0)
        self.assertEqual(counting_plus_plus_optimised([1, 5, 7, 8]), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)