import unittest

from line_segment import line_segment

class TestCases(unittest.TestCase):
    def test_line_segment(self):
        self.assertEqual(line_segment([[1,1],[1,2],[3,4],[3,5]]), False)
        self.assertEqual(line_segment([[1,1],[3,3],[4,6]]), False)
        self.assertEqual(line_segment([[1,1],[3,3],[7,7]]), True)
        self.assertEqual(line_segment([[-2,-4],[3,6]]), True)
        self.assertEqual(line_segment([[0,0],[1,1]]), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)