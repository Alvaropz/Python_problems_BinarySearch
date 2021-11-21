import unittest

from fibonacci_subset_sum import fibonacci_subset_sum

class TestCases(unittest.TestCase):
    def test_fibonacci_subset_sum(self):
        self.assertEqual(fibonacci_subset_sum(1), 1)
        self.assertEqual(fibonacci_subset_sum(2), 1)
        self.assertEqual(fibonacci_subset_sum(3), 1)
        self.assertEqual(fibonacci_subset_sum(4), 2)
        self.assertEqual(fibonacci_subset_sum(5), 1)
        self.assertEqual(fibonacci_subset_sum(6), 2)
        self.assertEqual(fibonacci_subset_sum(7), 2)
        self.assertEqual(fibonacci_subset_sum(22), 2)
        self.assertEqual(fibonacci_subset_sum(15), 2)
        self.assertEqual(fibonacci_subset_sum(123), 2)
        self.assertEqual(fibonacci_subset_sum(1038), 5)
        self.assertEqual(fibonacci_subset_sum(2091), 6)
        self.assertEqual(fibonacci_subset_sum(5763), 8)
        self.assertEqual(fibonacci_subset_sum(62871), 8)

if __name__ == "__main__":
    unittest.main(verbosity=2)