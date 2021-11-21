'''
You are given a string s containing lowercase and uppercase alphabet characters as well as digits from "0" to "9". 

Return whether s is a palindrome if we only consider the lowercase alphabet characters.
'''

# Binary Search - Your code took 32 milliseconds — faster than 80.54% in Python.

import string

def noisy_palindrome(s):
    lower = string.ascii_lowercase
    f_s = ""
    for char in s:
        if char in lower:
            f_s += char
    if f_s == f_s[::-1]:
        return True
    return False
