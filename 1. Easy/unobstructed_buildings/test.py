import unittest

from unobstructed_buildings import unobstructed_buildings

class TestCases(unittest.TestCase):
    def test_unobstructed_buildings(self):
        self.assertEqual(unobstructed_buildings([1, 5, 5, 2, 3]), [2, 4])
        self.assertEqual(unobstructed_buildings([]), [])
        self.assertEqual(unobstructed_buildings([1]), [0])
        self.assertEqual(unobstructed_buildings([1,5,7,5,2,3,2,1]), [2, 3, 5, 6, 7])

if __name__ == "__main__":
    unittest.main(verbosity=2)