import unittest

from colltaz_sequence import colltaz_f

class TestCases(unittest.TestCase):
    def test_colltaz(self):
        self.assertEqual(colltaz_f(11), 15)
        self.assertEqual(colltaz_f(15), 18)
        self.assertEqual(colltaz_f(5), 6)
        self.assertEqual(colltaz_f(12), 10)

if __name__ == "__main__":
    unittest.main(verbosity=2)