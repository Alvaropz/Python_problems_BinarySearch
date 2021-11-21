import unittest

from check_if_number_is_perfect_square import check_if_number_is_perfect_square

class TestCases(unittest.TestCase):
    def test_check_if_number_is_perfect_square(self):
        self.assertEqual(check_if_number_is_perfect_square(25), True)
        self.assertEqual(check_if_number_is_perfect_square(1), True)
        self.assertEqual(check_if_number_is_perfect_square(9), True)
        self.assertEqual(check_if_number_is_perfect_square(0), True)
        self.assertEqual(check_if_number_is_perfect_square(5), False)
        self.assertEqual(check_if_number_is_perfect_square(5), False)
        self.assertEqual(check_if_number_is_perfect_square(7), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)