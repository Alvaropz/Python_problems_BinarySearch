import unittest

from equal_piles import equal_piles

class TestCases(unittest.TestCase):
    def test_equal_piles(self):
        self.assertEqual(equal_piles([4,8,2]), 3)
        self.assertEqual(equal_piles([4,8,2,2,2,4,2]), 4)
        self.assertEqual(equal_piles([]),0)
        self.assertEqual(equal_piles([1]), 0)
        self.assertEqual(equal_piles([1,1,1,1,1,1,1,1,1,1,2]), 1)
        self.assertEqual(equal_piles([1,2,3,4,5,6,7,8,9,10]), 45)
        self.assertEqual(equal_piles([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7]), 112)
        self.assertEqual(equal_piles([9,8,7,6,5,692,45056,2,45,1,5,78,3,6,81,2,3,5,7,9,5,4,6,8,45,6,48,48,1,23,3,6,37,48,56,85,9,5,2345,62,245,6345,63,2345634,67,354]), 456)

if __name__ == "__main__":
    unittest.main(verbosity=2)