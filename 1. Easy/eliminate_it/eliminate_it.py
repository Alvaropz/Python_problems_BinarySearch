'''
Given a lowercase alphabet string s, remove all “y” and “xz” in the string in one iteration.
'''

# Binary Search - Your code took 17 milliseconds — faster than 46.70% in Python

def eliminate_it(s):
    s = s.replace('xz','')
    s = s.replace('y','')
    return s