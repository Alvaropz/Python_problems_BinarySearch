import unittest

from double_reverse_swap import double_reverse_swap

class TestCases(unittest.TestCase):
    def test_double_reverse_swap(self):
        self.assertEqual(double_reverse_swap(1), "xxyxxy")
        self.assertEqual(double_reverse_swap(2), "yxxyxx")
        self.assertEqual(double_reverse_swap(3), "xyyxyy")
        self.assertEqual(double_reverse_swap(4), "xyyxyyxyyxyy")
        self.assertEqual(double_reverse_swap(5), "yyxyyxyyxyyx")
        self.assertEqual(double_reverse_swap(6), "xxyxxyxxyxxy")
        self.assertEqual(double_reverse_swap(7), "xxyxxyxxyxxyxxyxxyxxyxxy")
        self.assertEqual(double_reverse_swap(8), "yxxyxxyxxyxxyxxyxxyxxyxx")
        self.assertEqual(double_reverse_swap(9), "xyyxyyxyyxyyxyyxyyxyyxyy")
        self.assertEqual(double_reverse_swap(10), "xyyxyyxyyxyyxyyxyyxyyxyyxyyxyyxyyxyyxyyxyyxyyxyy")


if __name__ == "__main__":
    unittest.main(verbosity=2)