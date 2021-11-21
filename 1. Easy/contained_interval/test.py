import unittest

from contained_interval import contained_interval

class TestCases(unittest.TestCase):
    def test_contained_interval(self):
        self.assertEqual(contained_interval([[0, 4],[1, 4]]), True)
        self.assertEqual(contained_interval([[0, 2],[0, 0]]), True)
        self.assertEqual(contained_interval([[2, 3],[4, 5]]), False)
        self.assertEqual(contained_interval([[1, 10],[5, 6]]), True)
        self.assertEqual(contained_interval([[2, 5],[4, 7]]), False)
        self.assertEqual(contained_interval([[10, 11],[3, 7]]), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)