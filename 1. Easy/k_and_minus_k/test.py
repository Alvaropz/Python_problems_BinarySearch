import unittest

from k_and_minus_k import k_and_minus_k, k_and_minus_k_dictionary

class TestCases(unittest.TestCase):
    def test_k_and_minus_k(self):
        self.assertEqual(k_and_minus_k([-4,1,8,-5,4,-8,6,2,7]), 8)
        self.assertEqual(k_and_minus_k([-1, -2, -3, -4, 0, 3, 4]), 4)
        self.assertEqual(k_and_minus_k([1, 2, 0, 3, 4]), 0)
        self.assertEqual(k_and_minus_k([5]), -1)
        self.assertEqual(k_and_minus_k([9, -9]), 9)
        self.assertEqual(k_and_minus_k([-6, 6]), 6)

    def test_k_and_minus_k_dictionary(self):
        self.assertEqual(k_and_minus_k_dictionary([-4,1,8,-5,4,-8,6,2,7]), 8)
        self.assertEqual(k_and_minus_k_dictionary([-1, -2, -3, -4, 0, 3, 4]), 4)
        self.assertEqual(k_and_minus_k_dictionary([1, 2, 0, 3, 4]), 0)
        self.assertEqual(k_and_minus_k_dictionary([5]), -1)
        self.assertEqual(k_and_minus_k_dictionary([9, -9]), 9)
        self.assertEqual(k_and_minus_k_dictionary([-6, 6]), 6)


if __name__ == "__main__":
    unittest.main(verbosity=2)