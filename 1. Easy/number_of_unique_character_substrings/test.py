import unittest

from number_of_unique_character_substrings import number_of_unique_character_substrings

class TestCases(unittest.TestCase):
    def test_number_of_unique_character_substrings(self):
        self.assertEqual(number_of_unique_character_substrings("aaabc"), 8)
        self.assertEqual(number_of_unique_character_substrings("f"), 1)
        self.assertEqual(number_of_unique_character_substrings("rb"), 2)
        self.assertEqual(number_of_unique_character_substrings("abc"), 3)
        self.assertEqual(number_of_unique_character_substrings("abbccc"), 10)
        self.assertEqual(number_of_unique_character_substrings("julian"), 6)
        self.assertEqual(number_of_unique_character_substrings("aabbccddffgghh"), 21)
        self.assertEqual(number_of_unique_character_substrings("aaabbccccddd"), 25)
        self.assertEqual(number_of_unique_character_substrings("afaabbfccfccddfd"), 21)


if __name__ == "__main__":
    unittest.main(verbosity=2)