import unittest

from unique_fractions import unique_fractions

class TestCases(unittest.TestCase):
    def test_unique_fractions(self):
        self.assertEqual(unique_fractions([[8,4],[2,1],[7,3],[14,6],[10,2],[-3,6]]), [[-1, 2],[2, 1],[7, 3],[5, 1]])


if __name__ == "__main__":
    unittest.main(verbosity=2)