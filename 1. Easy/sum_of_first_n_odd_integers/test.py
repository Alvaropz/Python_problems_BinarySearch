import unittest

from sum_of_first_n_odd_integers import sum_of_first_n_odd_integers, sum_of_first_n_odd_integers_optimised

class TestCases(unittest.TestCase):
    def test_sum_of_first_n_odd_integers(self):
        self.assertEqual(sum_of_first_n_odd_integers(1), 1)
        self.assertEqual(sum_of_first_n_odd_integers(2), 4)
        self.assertEqual(sum_of_first_n_odd_integers(3), 9)
        self.assertEqual(sum_of_first_n_odd_integers(4), 16)
        self.assertEqual(sum_of_first_n_odd_integers(5), 25)

    def test_sum_of_first_n_odd_integers(self):
        self.assertEqual(sum_of_first_n_odd_integers_optimised(1), 1)
        self.assertEqual(sum_of_first_n_odd_integers_optimised(2), 4)
        self.assertEqual(sum_of_first_n_odd_integers_optimised(3), 9)
        self.assertEqual(sum_of_first_n_odd_integers_optimised(4), 16)
        self.assertEqual(sum_of_first_n_odd_integers_optimised(5), 25)


if __name__ == "__main__":
    unittest.main(verbosity=2)