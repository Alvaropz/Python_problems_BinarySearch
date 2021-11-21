import unittest

from vowels_and_consonants_sort import vowels_and_consonants

class TestCases(unittest.TestCase):
    def test_string_sorted(self):
        self.assertEqual(vowels_and_consonants("decalin"), "aeicdln")
        self.assertEqual(vowels_and_consonants("fitoepdlbjfhd"), "eiobddffhjlpt")
        self.assertEqual(vowels_and_consonants("aeioubcdf"), "aeioubcdf")
        self.assertEqual(vowels_and_consonants("bcdfaeiou"), "aeioubcdf")
        self.assertEqual(vowels_and_consonants("abecidofu"), "aeioubcdf")

if __name__ == "__main__":
    unittest.main(verbosity=2)