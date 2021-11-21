import unittest

from just_average import just_average

class TestCases(unittest.TestCase):
    def test_just_average(self):
        self.assertEqual(just_average([1, 2, 3, 10], 2), True)
        self.assertEqual(just_average([1, 1], 1), True)
        self.assertEqual(just_average([1, 2, 3], 3), False)
        self.assertEqual(just_average([1, 2, 3, 4 ,5], 3), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)