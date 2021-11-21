import unittest

from toeplitz_matrix import toeplitz_matrix

class TestCases(unittest.TestCase):
    def test_toeplitz_matrix(self):
        self.assertEqual(toeplitz_matrix([[0,1,2],[3,0,1],[4,3,0],[5,4,3]]), True)
        self.assertEqual(toeplitz_matrix([[0,1,2],[3,0,1],[4,3,0],[5,4,9]]), False)
        self.assertEqual(toeplitz_matrix([[0,1,2],[3,7,1],[4,3,0],[5,4,3]]), False)
        self.assertEqual(toeplitz_matrix([[0,1,2,5],[3,0,1,2]]), True)
        self.assertEqual(toeplitz_matrix([[0,1,2,5,7,9],[3,0,1,2,5,7,8]]), True)
        self.assertEqual(toeplitz_matrix([[0,1,2,5]]), True)
        self.assertEqual(toeplitz_matrix([[]]), True)
        self.assertEqual(toeplitz_matrix([[1,1,1,1],[1,1,1,1]]), True)
        self.assertEqual(toeplitz_matrix([[0,1,2,5],[0,2,2,5]]), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)