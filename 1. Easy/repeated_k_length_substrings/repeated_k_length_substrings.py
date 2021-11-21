'''
Given a string s and an integer k, return the number of k-length substrings that occur more than once in s.
'''

# Binary Search - Your code took 86 milliseconds — faster than 48.57% in Python.

from collections import Counter

def repeated_k_length_substrings(s, k):
    substrings = [s[index:index+k] for index in range(len(s)) if len(s[index:index+k]) == k]
    dict_counting = Counter(substrings)
    total = 0
    for k in dict_counting:
        if dict_counting[k] > 1:
            total += 1
    return total

# Binary Search - Your code took 64 milliseconds — faster than 86.43% in Python.

def repeated_k_length_substrings_optimised(s, k):
    substrings = [s[index:index+k] for index in range(len(s)-k+1)] 
    dict_counting = Counter(substrings)
    total = 0
    for k in dict_counting:
        if dict_counting[k] > 1:
            total += 1
    return total