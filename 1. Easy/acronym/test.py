import unittest

from acronym import acronym

class TestCases(unittest.TestCase):
    def test_acronym(self):
        self.assertEqual(acronym("For your information"), "FYI")
        self.assertEqual(acronym("National Aeronautics and Space Administration"),"NASA")
        self.assertEqual(acronym("Long life to The Queen"), "LLTTQ")

if __name__ == "__main__":
    unittest.main(verbosity=2)