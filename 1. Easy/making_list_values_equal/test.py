import unittest

from making_list_values_equal import making_list_values_equals

class TestCases(unittest.TestCase):
    def test(self):
        self.assertEqual(making_list_values_equals([1,3,4,6,7,2,5]), 6)
        self.assertEqual(making_list_values_equals([1,3,4,6,5]), 5)
        self.assertEqual(making_list_values_equals([1,3,4]), 3)
        self.assertEqual(making_list_values_equals([2,1]), 1)
        self.assertEqual(making_list_values_equals([1,7,9,6,5]), 8)
        self.assertEqual(making_list_values_equals([2,5,10,16,24]), 22)

if __name__ == "__main__":
    unittest.main(verbosity=2)