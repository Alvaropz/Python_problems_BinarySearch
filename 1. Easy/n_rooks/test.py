import unittest

from n_rooks import n_rooks

class TestCases(unittest.TestCase):
    def test_n_rooks(self):
        self.assertEqual(n_rooks(1), 1)
        self.assertEqual(n_rooks(2), 2)
        self.assertEqual(n_rooks(3), 6)
        self.assertEqual(n_rooks(4), 24)
        self.assertEqual(n_rooks(5), 120)
        self.assertEqual(n_rooks(6), 720)
        self.assertEqual(n_rooks(7), 5040)
        self.assertEqual(n_rooks(8), 40320)
        self.assertEqual(n_rooks(9), 362880)
        self.assertEqual(n_rooks(10), 3628800)
        self.assertEqual(n_rooks(11), 39916800)
        self.assertEqual(n_rooks(12), 479001600)
        self.assertEqual(n_rooks(13), 6227020800)


if __name__ == "__main__":
    unittest.main(verbosity=2)