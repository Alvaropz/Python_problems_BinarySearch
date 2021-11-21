import unittest

from z_sum import z_sum

class TestCases(unittest.TestCase):
    def test_z_sum(self):
        self.assertEqual(z_sum([[1,2,3],[4,5,6],[7,8,9]]), 35)
        self.assertEqual(z_sum([[1,2,3],[4,5,6]]), 21)
        self.assertEqual(z_sum([[1,2,3]]), 6)
        self.assertEqual(z_sum([]), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)