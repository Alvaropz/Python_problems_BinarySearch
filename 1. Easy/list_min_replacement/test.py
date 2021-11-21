import unittest

from list_min_replacement import list_min_replacement

class TestCases(unittest.TestCase):
    def test_list_min_replacement(self):
        self.assertEqual(list_min_replacement([10, 5, 7, 9]), [0, 10, 5, 5])
        self.assertEqual(list_min_replacement([10, 1, 2, 8]), [0, 10, 1, 1])
        self.assertEqual(list_min_replacement([1, 2, 3, 4]), [0, 1, 1, 1])
        self.assertEqual(list_min_replacement([4, 3, 2, 1]), [0, 4, 3, 2])
        self.assertEqual(list_min_replacement([7, 5, 5, 4, 4, 6, 7, 8, 3, 3, 1]), [0, 7, 5, 5, 4, 4, 4, 4, 4, 3, 3])

if __name__ == "__main__":
    unittest.main(verbosity=2)