import unittest

from integer_to_base_three import integer_to_base_three

class TestCases(unittest.TestCase):
    def test_integer_to_base_three(self):
        self.assertEqual(integer_to_base_three(5), "12")
        self.assertEqual(integer_to_base_three(1), "1")
        self.assertEqual(integer_to_base_three(367465746), "221121110012020110")
        self.assertEqual(integer_to_base_three(-23452345243), "-2020112102201120121101")

if __name__ == "__main__":
    unittest.main(verbosity=2)