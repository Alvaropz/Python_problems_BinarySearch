import unittest

from picking_boxes import picking_boxes

class TestCases(unittest.TestCase):
    def test_picking_boxes(self):
        self.assertEqual(picking_boxes([4, 4, 1, 6, 6, 6, 1, 1, 1, 1]), [[4, 4], [1], [6, 6, 6], [1, 1, 1, 1]])
        self.assertEqual(picking_boxes([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), [[1], [2], [3], [4], [5], [6], [7], [8], [9], [0]])
        self.assertEqual(picking_boxes([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]), [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5]])
        self.assertEqual(picking_boxes([5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1]), [[5, 5, 5, 5, 5], [4, 4, 4, 4], [3, 3, 3], [2, 2], [1]])
        self.assertEqual(picking_boxes([11, 11]), [[11, 11]])
        self.assertEqual(picking_boxes([]), [])

if __name__ == "__main__":
    unittest.main(verbosity=2)