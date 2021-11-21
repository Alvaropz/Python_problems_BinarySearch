import unittest

from generate_primes import generate_primes, generate_primes_v2

class TestCases(unittest.TestCase):
    def test_generate_primes(self):
        self.assertEqual(generate_primes(0), [])
        self.assertEqual(generate_primes(10), [2, 3, 5, 7])
        self.assertEqual(generate_primes(3), [2, 3])
        self.assertEqual(generate_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(generate_primes(999999), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_generate_primes_v2s(self):
        self.assertEqual(generate_primes_v2(0), [])
        self.assertEqual(generate_primes_v2(10), [2, 3, 5, 7])
        self.assertEqual(generate_primes_v2(3), [2, 3])
        self.assertEqual(generate_primes_v2(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(generate_primes_v2(999999), [2, 3, 5, 7, 11, 13, 17, 19])


if __name__ == "__main__":
    unittest.main(verbosity=2)