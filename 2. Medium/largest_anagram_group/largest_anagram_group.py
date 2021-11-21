'''
Given a list of strings words, group all anagrams together and return the size of the largest grouping.
'''

# Binary Search - Your code took 107 milliseconds — faster than 99.16% in Python.

def largest_anagram_group(words):
    dict_anagrams = {}
    for anagram in words:
        sorted_string = "".join(sorted(anagram))
        if sorted_string in dict_anagrams:
            dict_anagrams[sorted_string] += 1
        else:
            dict_anagrams[sorted_string] = 1
    return max(dict_anagrams.values())
