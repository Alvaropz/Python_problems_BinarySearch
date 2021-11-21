import unittest

from smallest_intersecting_element import smallest_intersecting_element

class TestCases(unittest.TestCase):
    def test_smallest_intersecting_element(self):
        self.assertEqual(smallest_intersecting_element([[1,2,4],[4,9,9],[0,2,4]]), 4)
        self.assertEqual(smallest_intersecting_element([[1,2,3,5],[3,5,9,9],[0,2,3,5]]), 3)
        self.assertEqual(smallest_intersecting_element([[1,2,3,5],[6,7,8,9],[10,11,12,13]]), -1)
        self.assertEqual(smallest_intersecting_element([[1,2,3,5],[5,7,8,9],[1,11,12,13]]), -1)
        self.assertEqual(smallest_intersecting_element([[1,9,9,9],[1,9,9,9],[0,1,9,9]]), 1)
        self.assertEqual(smallest_intersecting_element([]), -1)
        self.assertEqual(smallest_intersecting_element([[]]), -1)
        self.assertEqual(smallest_intersecting_element([[0],[3],[0]]), -1)
        self.assertEqual(smallest_intersecting_element([[0],[0]]), 0)
        self.assertEqual(smallest_intersecting_element([[5]]), 5)

if __name__ == "__main__":
    unittest.main(verbosity=2)