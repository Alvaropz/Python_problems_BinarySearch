import unittest

from a_number_and_its_triple import ta_number_and_its_triple, a_number_and_its_triple_v2

class TestCases(unittest.TestCase):
    def test_a_number_and_its_triple(self):
        self.assertEqual(ta_number_and_its_triple([2, 3, 10, 7, 6]), True)
        self.assertEqual(ta_number_and_its_triple([0, 0]), True)
        self.assertEqual(ta_number_and_its_triple([0]), False)
        self.assertEqual(ta_number_and_its_triple([-6, 0]), False)
        self.assertEqual(ta_number_and_its_triple([-6, -18]), True)
    
    def test_a_number_and_its_triple_v2(self):
        self.assertEqual(a_number_and_its_triple_v2([2, 3, 10, 7, 6]), True)
        self.assertEqual(a_number_and_its_triple_v2([0, 0]), True)
        self.assertEqual(a_number_and_its_triple_v2([0]), False)
        self.assertEqual(a_number_and_its_triple_v2([-6, 0]), False)
        self.assertEqual(a_number_and_its_triple_v2([-6, -18]), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)