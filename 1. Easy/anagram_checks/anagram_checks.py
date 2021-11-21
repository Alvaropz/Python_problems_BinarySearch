'''
Given two strings s0 and s1, return whether they are anagrams of each other. 
Two words are anagrams when you can rearrange one to become the other. For example, "listen" and "silent" are anagrams.
'''

# Binary Search: Your code took 35 milliseconds — faster than 97.12% in Python

from collections import Counter

def anagram_checks(s0, s1):
    dict_s0 = Counter(s0)
    dict_s1 = Counter(s1)
    if dict_s0 == dict_s1:
        return True
    return False