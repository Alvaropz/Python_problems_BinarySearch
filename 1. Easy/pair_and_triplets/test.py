import unittest

from pair_and_triplets import pair_and_triplets

class TestCases(unittest.TestCase):
    def testPair_and_Triplets(self):
        self.assertEqual(pair_and_triplets("22222222"), True)
        self.assertEqual(pair_and_triplets("21112"), True)
        self.assertEqual(pair_and_triplets("55"), True)
        self.assertEqual(pair_and_triplets("111222"), False)
        self.assertEqual(pair_and_triplets("11111"), True)
        self.assertEqual(pair_and_triplets("225552"), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)