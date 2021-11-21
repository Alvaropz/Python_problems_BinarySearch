'''
You are given a string s and an integer k. Return the number of palindromes you can construct of length k using only letters in s. Letters can be used more than once.
'''

# Binary Search - Your code took 2 milliseconds — faster than 63.78% in Python. Both functions run with a 63.78% efficiency.

import math

def palindrome_count_dict(s, k):
    dict_counting = list(dict.fromkeys(s))
    return len(dict_counting) ** math.ceil(k/2)

def palindrome_count_set(s, k):
    set_of_elements = set()
    for char in s:
        if not char in set_of_elements:
            set_of_elements.add(char)
    return len(set_of_elements) ** math.ceil(k/2)