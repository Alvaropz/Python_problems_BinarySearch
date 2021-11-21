import unittest

from base_three_to_integer import base_three_to_integer

class TestCases(unittest.TestCase):
    def test_base_three_to_integer(self):
        self.assertEqual(base_three_to_integer("1"), 1)
        self.assertEqual(base_three_to_integer("10"), 3)
        self.assertEqual(base_three_to_integer("12"), 5)
        self.assertEqual(base_three_to_integer("21"), 7)
        self.assertEqual(base_three_to_integer("120"), 15)
        self.assertEqual(base_three_to_integer("1201"), 46)
        self.assertEqual(base_three_to_integer("12010"), 138)
        self.assertEqual(base_three_to_integer("120102"), 416)
        self.assertEqual(base_three_to_integer("1201021"), 1249)
        self.assertEqual(base_three_to_integer("12010210"), 3747)
        self.assertEqual(base_three_to_integer("120102102"), 11243)
        self.assertEqual(base_three_to_integer("1201021021"), 33730)

if __name__ == "__main__":
    unittest.main(verbosity=2)