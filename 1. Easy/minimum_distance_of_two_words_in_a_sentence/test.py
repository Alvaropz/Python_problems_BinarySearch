import unittest

from minimum_distance_of_two_words_in_a_sentence import minimum_distance_of_two_words_in_a_sentence

class TestCases(unittest.TestCase):
    def test_minimum_distance_of_two_words_in_a_sentence(self):
        self.assertEqual(minimum_distance_of_two_words_in_a_sentence("dog cat hello cat dog dog hello cat world", "hello", "world"), 1)
        self.assertEqual(minimum_distance_of_two_words_in_a_sentence("dog trainers zoom cat hello world", "woof", "meow"), -1)
        self.assertEqual(minimum_distance_of_two_words_in_a_sentence("dog cat hello cat dog dog hello cat world", "hello", "world"), 1)
        self.assertEqual(minimum_distance_of_two_words_in_a_sentence("dog cat hello world", "hello", "world"), 0)
        self.assertEqual(minimum_distance_of_two_words_in_a_sentence("dog cat hello cat dog dog hello cat", "hello", "world"), -1)
        self.assertEqual(minimum_distance_of_two_words_in_a_sentence("dog cat cat dog dog cat world", "hello", "world"), -1)
        self.assertEqual(minimum_distance_of_two_words_in_a_sentence("hello hello dog cat cat dog dog cat world", "hello", "world"), 6)
        self.assertEqual(minimum_distance_of_two_words_in_a_sentence("hello hello cow dog cat cat dog dog cat world world", "hello", "world"), 7)
        self.assertEqual(minimum_distance_of_two_words_in_a_sentence("hello hello cow dog cat hello world dog cat world world", "hello", "world"), 0)
        self.assertEqual(minimum_distance_of_two_words_in_a_sentence("hello hello dog cat cat dog dog cat world", "hello", "word"), -1)
        self.assertEqual(minimum_distance_of_two_words_in_a_sentence("dog cat cat dog dog cat hello cow world", "hello", "world"), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)