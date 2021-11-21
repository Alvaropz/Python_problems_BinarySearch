import unittest

from number_flip_123 import number_flip_123

class TestCases(unittest.TestCase):
    def test_number_flip_123(self):
        self.assertEqual(number_flip_123(123), 323)
        self.assertEqual(number_flip_123(333), 333)
        self.assertEqual(number_flip_123(321), 331)
        self.assertEqual(number_flip_123(331), 333)
        self.assertEqual(number_flip_123(3331232313), 3333232313)

if __name__ == "__main__":
    unittest.main(verbosity=2)