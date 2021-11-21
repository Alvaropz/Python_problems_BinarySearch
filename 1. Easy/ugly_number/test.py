import unittest

from ugly_number import ugly_number

class TestCases(unittest.TestCase):
    def test_ugly_number(self):
        self.assertEqual(ugly_number(0), False)
        self.assertEqual(ugly_number(1), True)
        self.assertEqual(ugly_number(2), True)
        self.assertEqual(ugly_number(3), True)
        self.assertEqual(ugly_number(4), True)
        self.assertEqual(ugly_number(5), True)
        self.assertEqual(ugly_number(6), True)
        self.assertEqual(ugly_number(7), False)
        self.assertEqual(ugly_number(8), True)
        self.assertEqual(ugly_number(9), True)
        self.assertEqual(ugly_number(10), True)
        self.assertEqual(ugly_number(14), False)
        self.assertEqual(ugly_number(22),False)
        self.assertEqual(ugly_number(51), False)
        self.assertEqual(ugly_number(111), False)
        self.assertEqual(ugly_number(1254), False)
        self.assertEqual(ugly_number(581273), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)