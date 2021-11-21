'''
Given a string s, determine whether any anagram of s is a palindrome.
'''

# Binary Search - Your code took 12 milliseconds — faster than 96.94% in Python.

from collections import Counter

def palindromic_anagram(s):
    dict_s = Counter(s)
    list_odds = len(list(filter(lambda x: x % 2 != 0, dict_s.values())))
    if list_odds > 1:
        return False
    return True