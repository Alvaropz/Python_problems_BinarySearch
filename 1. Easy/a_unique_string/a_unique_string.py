'''
Given a string s, determine whether it has all unique characters.
'''
#Your code took 3 milliseconds — faster than 22.51% in Python

from collections import Counter

def a_unique_string(s):
    dict_count = Counter(s)
    for value in dict_count.values():
        if value > 1:
            return False
    return True

#Your code took 1 millisecond — faster than 99.94% in Python

def a_unique_string_optimised(s):
    count = 0
    for outer_char in s:
        for inner_char in s:
            if outer_char == inner_char:
                count += 1
            if count > 1:
                return False
        count = 0
    return True