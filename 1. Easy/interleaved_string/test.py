import unittest

from interleaved_string import interleaved_string

class TestCases(unittest.TestCase):
    def test_interleaved_string(self):
        self.assertEqual(interleaved_string("abc", "xyz"), "axbycz")
        self.assertEqual(interleaved_string("abc", "x"), "axbc")
        self.assertEqual(interleaved_string("a", "xyz"), "axyz")
        self.assertEqual(interleaved_string("", "xyz"), "xyz")
        self.assertEqual(interleaved_string("abc", ""), "abc")


if __name__ == "__main__":
    unittest.main(verbosity=2)