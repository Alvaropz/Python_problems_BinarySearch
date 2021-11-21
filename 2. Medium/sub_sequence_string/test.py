import unittest

from sub_sequence_string import sub_sequence_string

class TestCases(unittest.TestCase):
    def test_sub_sequence_string(self):
        self.assertEqual(sub_sequence_string("ppl", "apple"), True)
        self.assertEqual(sub_sequence_string("ale", "apple"), True)
        self.assertEqual(sub_sequence_string("elppa", "apple"), False)
        self.assertEqual(sub_sequence_string("anno", "anno"), True)
        self.assertEqual(sub_sequence_string("", "cow"), True)
        self.assertEqual(sub_sequence_string("", ""), True)
        self.assertEqual(sub_sequence_string("boat", ""), False)
        self.assertEqual(sub_sequence_string("titanic", "tbiotaantic"), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)