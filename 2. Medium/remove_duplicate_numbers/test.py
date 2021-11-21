import unittest

from remove_duplicate_numbers import remove_duplicate_numbers

class TestCases(unittest.TestCase):
    def test_remove_duplicate_numbers(self):
        self.assertEqual(remove_duplicate_numbers([1,3,5,0,3,5,8]), [1, 0, 8])
        self.assertEqual(remove_duplicate_numbers([1,3,5,0,3,5,8,8,0]), [1])
        self.assertEqual(remove_duplicate_numbers([1,3,5,1,0,3,5,8,8,0]), [])
        self.assertEqual(remove_duplicate_numbers([1,5,0,3,8]), [1, 5, 0, 3, 8])
        self.assertEqual(remove_duplicate_numbers([]), [])

if __name__ == "__main__":
    unittest.main(verbosity=2)