import unittest

from k_compare import k_compare

class TestCases(unittest.TestCase):
    def test_k_compare(self):
        self.assertEqual(k_compare([5,-3,99,10], [32,5,29,7,13,10,9,12,27,51,83,75,43,59], 5), 3)
        self.assertEqual(k_compare([5,-3,99,10,23,51,68,99,103,115,183,143,173,190,214,133], [32,5,29,7,13,10,9,12,27,51,83,75,43,59], 5), 4)
        self.assertEqual(k_compare([51,68,99,103,115,183,143,173,190,214,133], [32,5,29,7,13,10,9,12,27,51,83,75,43,59], 5), 0)
        self.assertEqual(k_compare([51,68,99,103,115,183,143,173,190,214,133], [32,5,29,7,13,10,9,12,27,51,83,75,43,59], 4), 0)
        self.assertEqual(k_compare([51,68,99,103,115,183,143,173,190,214,133], [32,5,29,7,13,10,9,12,27,51,83,75,43,59], 3), 1)
        self.assertEqual(k_compare([51,68,99,103,115,183,143,173,190,214,133], [32,5,29,7,13,10,9,12,27,51,83,75,43,59], 2), 2)
        self.assertEqual(k_compare([51,68,99,103,115,183,143,173,190,214,133,40,37,23], [32,5,29,7,13,10,9,12,27,51,83,75,43,59], 2), 5)
        self.assertEqual(k_compare([51,68,99,103,115,183,143,173,190,214,133,40,37,23], [], 0), 14)
        self.assertEqual(k_compare([5,-3,99,10], [32,5,29,7,13,10,9,12,27,51,83,75,43,59], 4), 3)
        self.assertEqual(k_compare([5,-3,99,10], [32,5,29,7,13,10,9,12,27,51,83,75,43,59], 3), 3)
        self.assertEqual(k_compare([5,-3,99,10], [32,5,29,7,13,10,9,12,27,51,83,75,43,59], 2), 3)
        self.assertEqual(k_compare([5,-3,99,10], [32,5,29,7,13,10,9,12,27,51,83,75,43,59], 0), 4)
        self.assertEqual(k_compare([5,-3,99,10], [32,5,29,7,13,10], 0), 4)
        self.assertEqual(k_compare([5,-3,99,10], [5,29,7,13,10], 3), 2)
        self.assertEqual(k_compare([5,-3,99,10], [5,7,13,10], 2), 2)
        self.assertEqual(k_compare([5,-3,99,10], [5,7], 2), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)