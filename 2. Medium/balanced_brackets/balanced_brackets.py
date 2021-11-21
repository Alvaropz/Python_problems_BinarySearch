'''
You're given a string s consisting solely of "(" and ")". Return whether the parentheses are balanced.
'''

# Binary Search - Your code took 27 milliseconds — faster than 38.37% in Python.

def balanced_brackets(s):
    i = 0
    j = len(s)-1
    count = 0
    while i <= j:
        if s[i] == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
        i += 1
    if count != 0:
        return False
    return True