'''
Given a lowercase alphabet string s, return a string with all the vowels of s in sorted order followed by all the consonants of s in sorted order.

Note: vowels are ["a", "e", "i", "o", "u"] and consonants are all other characters.
'''

# Binary Search - Your code took 31 milliseconds — faster than 52.63% in Python.

import re

def vowels_and_consonants(s):
    vowels = re.sub("[^a|e|i|o|u]", "", s)
    consonants = re.sub("a|e|i|o|u", "", s)
    vowels_list = sorted([vowel for vowel in vowels])
    consonants_list = sorted([consonant for consonant in consonants])
    return ("").join(vowels_list) + ("").join(consonants_list)