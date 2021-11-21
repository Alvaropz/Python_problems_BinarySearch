import unittest

from counting_dinosaurs import counting_dinosaurs

class TestCases(unittest.TestCase):
    def test_counting_dinosaurs(self):
        self.assertEqual(counting_dinosaurs("abacabC", "bC"), 3)
        self.assertEqual(counting_dinosaurs("bb", "bbb"), 2)
        self.assertEqual(counting_dinosaurs("bB", "abc"), 1)
        self.assertEqual(counting_dinosaurs("abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)