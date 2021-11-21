'''
Given a lowercase alphabet string s, return the index of the first recurring character in it. If there are no recurring characters, return -1.
'''

# Binary Search - Your code took 8 milliseconds — faster than 98.95% in Python.

def recurring_character(s):
    new_set = set()
    for index, char in enumerate(s):
        if not char in new_set:
            new_set.add(char)
        else:
            return index
    return -1