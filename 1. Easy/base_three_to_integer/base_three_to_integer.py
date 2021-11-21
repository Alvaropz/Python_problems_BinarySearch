'''
Given a string s representing a number in base 3 (consisting only of 0, 1, or 2), return its decimal integer equivalent. 

This should be implemented directly without using a built-in function.
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python.

def base_three_to_integer(s):
    i = 0
    j = len(s)-1
    n = 0
    while i < j:
        n += int(s[i])
        n *= 3
        i += 1
    return n + int(s[i])