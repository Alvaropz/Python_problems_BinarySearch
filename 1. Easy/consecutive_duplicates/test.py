import unittest

from consecutive_duplicates import consecutive_duplicates

class TestCases(unittest.TestCase):
    def test_consecutive_duplicates(self):
        self.assertEqual(consecutive_duplicates("YYYXYXX"), "YXYX")
        self.assertEqual(consecutive_duplicates("YYYY"), "Y")
        self.assertEqual(consecutive_duplicates("XX"), "X")
        self.assertEqual(consecutive_duplicates("Y"), "Y")
        self.assertEqual(consecutive_duplicates("YYYXYXXXYXXXYXYYYYXYYXYXYXYYYYXY"), "YXYXYXYXYXYXYXYXYXY")

if __name__ == "__main__":
    unittest.main(verbosity=2)