import unittest

from lexicographic_swap import lexicographic_swap

class TestCases(unittest.TestCase):
    def test_lexicographic_swap(self):
        self.assertEqual(lexicographic_swap("gxlavgh"), "axlgvgh")
        self.assertEqual(lexicographic_swap("rhb"), "bhr")
        self.assertEqual(lexicographic_swap("abb"), "abb")
        self.assertEqual(lexicographic_swap("bab"), "abb")
        self.assertEqual(lexicographic_swap("cbca"), "abcc")
        self.assertEqual(lexicographic_swap("aabcdhjaka"), "aaacdhjakb")

if __name__ == "__main__":
    unittest.main(verbosity=2)