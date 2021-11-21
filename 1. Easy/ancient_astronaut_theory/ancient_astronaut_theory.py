'''
You are given a string dictionary, representing a partial lexicographic ordering of ancient astronauts' dictionary. 
Given a string s, return whether it's a lexicographically sorted string according to this ancient astronaut dictionary.
'''

# Binary Search - Your code took 6 milliseconds — faster than 94.84% in Python.

def ancient_astronaut_theory(dictionary, s):
    index_ref = 0
    last_index = 0
    for char in s:
        if char in dictionary:
            index_ref = dictionary.index(char)
            if index_ref >= last_index:
                last_index = index_ref
            else:
                return False
    return True
