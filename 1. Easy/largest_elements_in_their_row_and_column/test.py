import unittest

from largest_elements_in_their_row_and_column import largest_elements_in_their_row_and_column

class TestCases(unittest.TestCase):
    def test_largest_elements_in_their_row_and_column(self):
        self.assertEqual(largest_elements_in_their_row_and_column([[0,0,1,0],[1,0,0,0],[0,1,0,0],[0,0,0,1]]), 4)
        self.assertEqual(largest_elements_in_their_row_and_column([[0,1],[1,0]]), 2)
        self.assertEqual(largest_elements_in_their_row_and_column([[1,0,1,0],[1,0,0,0],[0,1,0,0],[0,0,0,1]]), 2)
        self.assertEqual(largest_elements_in_their_row_and_column([[1,1,1],[0,1,0],[0,0,1]]), 0)
        self.assertEqual(largest_elements_in_their_row_and_column([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]), 5)

if __name__ == "__main__":
    unittest.main(verbosity=2)