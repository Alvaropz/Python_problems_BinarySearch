'''
Given a lowercase alphabet string s, return the total number of substrings that contain one unique character.
'''

# Binary Search - Your code took 15 milliseconds — faster than 69.46% in Python.

def number_of_unique_character_substrings(s):
    if len(s) == 1:
        return 1
    i = 0
    j = len(s)
    total = 0
    while i+1 < j:
        if s[i] == s[i+1]:
            temp_count = 1
            while i+1 < j and s[i] == s[i+1]:
                temp_count += 1
                i += 1
            i += 1
            while temp_count > 0:
                total += temp_count
                temp_count -= 1
        else:
            total += 1
            i += 1
    if s[-1] != s[-2]:
        total += 1
    return total