'''
Consider the following sequence of strings:

xxy
xxyxxy
yxxyxx
xyyxyy
xyyxyyxyyxyy
...
The pattern to obtain the next value is the following, starting with xxy as the first term:

If we are at the start of the pattern, double the string.
If the last operation was doubling, reverse the string.
If the last operation was reversing, swap all xs with ys and vice versa.
Repeat.
Given n, return the nth value (0-indexed) from this sequence.
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python.

def double_reverse_swap(n):
    given_s = "xxy"
    pattern = 0
    actions = 0
    while actions < n:
        if pattern == 0:
            given_s *= 2
        elif pattern == 1:
            given_s = given_s[::-1]
        elif pattern == 2:
            given_s = given_s.replace('x', '%temp%').replace('y', 'x').replace('%temp%', 'y') 
            pattern = -1
        actions += 1
        pattern += 1
    return given_s