import unittest

from pythagorean_triplets import pythagorean_triplets

class TestCases(unittest.TestCase):
    def test_pythagorean_triplets(self):
        self.assertEqual(pythagorean_triplets([5, 1, 7, 4, 3]), True)
        self.assertEqual(pythagorean_triplets([1, 2, 3]), False)
        self.assertEqual(pythagorean_triplets([0]), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)