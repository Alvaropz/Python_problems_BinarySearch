import unittest

from selling_products import selling_products

class TestCases(unittest.TestCase):
    def test_selling_products(self):
        self.assertEqual(selling_products([1,1,1,0,0], 2), 1)
        self.assertEqual(selling_products([0,0,1,1,2,3], 2), 2)
        self.assertEqual(selling_products([1,1,1,0,0,2,3,4,5], 2), 4)
        self.assertEqual(selling_products([1,1,1,0,0,2,3,4,5], 0), 6)
        self.assertEqual(selling_products([1,2,3,4,5,6], 2), 4)
        self.assertEqual(selling_products([1,1,1,0,0], 3), 1)
        self.assertEqual(selling_products([1,1,1,0,0,1,1,1,1,1,2,2,2,3,4,5,3,4,6,7,2,5,7,2,3,5,3,4,4,6,3,3,2,3,7,6,2,4,7,8,9], 3), 8)
        self.assertEqual(selling_products([1,1,1,0,0,1,1,1,1,1,2,2,2,3,4,5,3,4,6,7,2,5,7,2,4,5,3,4,4,6,6,3,2,3,7,6,2,4,7,8,9], 4), 7)
        self.assertEqual(selling_products([1,1,1,0,0,1,1,1,1,1,2,2,2,3,4,5,3,4,6,7,2,5,7,2,4,5,3,4,4,6,6,3,2,3,7,6,2,4,7,8,9], 5), 7)
        self.assertEqual(selling_products([1,1,1,0,0,1,1,1,1,1,2,2,2,3,4,5,3,4,6,7,2,5,7,2,4,5,3,4,4,6,6,3,2,3,7,6,2,4,7,8,9], 6), 7)
        self.assertEqual(selling_products([1,1,1,0,0,1,1,1,1,1,2,2,2,3,4,5,3,4,6,7,2,5,7,2,4,5,3,4,4,6,6,3,2,3,7,6,2,4,7,8,9], 10), 6)
        self.assertEqual(selling_products([1,1,1,0,0,1,1,1,1,1,2,2,2,3,4,5,3,4,6,7,2,5,7,2,4,5,3,4,4,6,6,3,2,3,7,6,2,4,7,8,9], 20), 3)
        self.assertEqual(selling_products([1,1,1,0,0,1,1,1,1,1,2,2,2,3,4,5,3,4,6,7,2,5,7,2,4,5,3,4,4,6,6,3,2,3,7,6,2,4,7,8,9,10,11,12,13,14,15,16,17,18,20,30,10,19,16,18], 12), 11)
        self.assertEqual(selling_products([], 3), 0)
        self.assertEqual(selling_products([], 0), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)