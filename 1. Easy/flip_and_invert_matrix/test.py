import unittest

from flip_and_invert_matrix import flip_and_invert_matrix

class TestCases(unittest.TestCase):
    def test_flip_and_invert_matrix(self):
        self.assertEqual(flip_and_invert_matrix([[1,1,0],[0,0,1],[0,0,0]]), [[1, 0, 0],[0, 1, 1],[1, 1, 1]])
        self.assertEqual(flip_and_invert_matrix([[0,0,0],[0,0,0],[0,0,0]]), [[1, 1, 1],[1, 1, 1],[1, 1, 1]])
        self.assertEqual(flip_and_invert_matrix([[0,0,1],[0,0,1],[0,0,1]]), [[0, 1, 1], [0, 1, 1], [0, 1, 1]])



if __name__ == "__main__":
    unittest.main(verbosity=2)