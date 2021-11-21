import unittest

from seat_arrangement import seat_arrangement

class TestCases(unittest.TestCase):
    def test_seat_arrangement(self):
        self.assertEqual(seat_arrangement([1, 0, 1], 0), True)
        self.assertEqual(seat_arrangement([0, 0], 1), True)
        self.assertEqual(seat_arrangement([], 1), False)
        self.assertEqual(seat_arrangement([], 0), True)
        self.assertEqual(seat_arrangement([0], 1), True)
        self.assertEqual(seat_arrangement([0, 0, 1, 0, 0, 0, 1], 2), True)
        self.assertEqual(seat_arrangement([0, 0, 0, 0, 0, 0, 0], 3), True)
        self.assertEqual(seat_arrangement([1, 0, 1, 0, 1, 0, 0], 3), False)
        self.assertEqual(seat_arrangement([0, 1, 0], 1), False)
        self.assertEqual(seat_arrangement([0, 0, 0], 1), True)
        self.assertEqual(seat_arrangement([1, 0, 0], 1), True)
        self.assertEqual(seat_arrangement([1, 0, 1], 1), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)