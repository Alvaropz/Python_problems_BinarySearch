import unittest

from transpose_of_a_matrix import transpose_of_a_matrix

class TestCases(unittest.TestCase):
    def test_transpose_of_a_matrix(self):
        self.assertEqual(transpose_of_a_matrix([[1,2,3],[4,5,6],[7,8,9]]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        self.assertEqual(transpose_of_a_matrix([[1,2,3,4],[4,5,6,7],[7,8,9,10],[8,0,34,12]]), [[1, 4, 7, 8], [2, 5, 8, 0], [3, 6, 9, 34], [4, 7, 10, 12]])
        self.assertEqual(transpose_of_a_matrix([[5,10],[15,20]]), [[5, 15], [10, 20]])
        self.assertEqual(transpose_of_a_matrix([]), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)