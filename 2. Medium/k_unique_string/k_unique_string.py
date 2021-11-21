'''
Given a string s of lowercase alphabet characters, and an integer k, return the minimum number of changes needed in the string (one change involves changing a single character to any other character) so that the resulting string has at most k distinct characters.
'''

# Binary Search - Your code took 12 milliseconds — faster than 98.14% in Python.

from collections import Counter

def k_unique_string(s, k):
    dict_counting = Counter(s)
    count = 0
    sorted_dict = {k: v for k, v in sorted(dict_counting.items(), key=lambda item: item[1])}
    list_unique_chars = list(sorted_dict.keys())
    while len(list_unique_chars) > k:
        count += sorted_dict[list_unique_chars[0]]
        list_unique_chars.pop(0)
    return count