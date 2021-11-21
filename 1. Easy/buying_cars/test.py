import unittest

from buying_cars import buying_cars

class TestCases(unittest.TestCase):
    def test_buying_cars(self):
        self.assertEqual(buying_cars([90, 30, 20, 40, 90], 95), 3)
        self.assertEqual(buying_cars([90], 90), 1)
        self.assertEqual(buying_cars([30], 1), 0)
        self.assertEqual(buying_cars([54], 55), 1)
        self.assertEqual(buying_cars([340, 405], 745), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)