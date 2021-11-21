import unittest

from square_of_a_list import square_of_a_list

class TestCases(unittest.TestCase):
    def test_square_of_a_list(self):
        self.assertEqual(square_of_a_list([3, 1, 4, 7]), [1, 9, 16, 49])
        self.assertEqual(square_of_a_list([0, 1, 2, 3, 4]), [0, 1, 4, 9, 16])
        self.assertEqual(square_of_a_list([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]), [1, 9, 25, 49, 81, 121, 169, 225, 289, 361])
        self.assertEqual(square_of_a_list([3, 3, 3, 3, 4, 4, 4, 4]), [9, 9, 9, 9, 16, 16, 16, 16])

if __name__ == "__main__":
    unittest.main(verbosity=2)