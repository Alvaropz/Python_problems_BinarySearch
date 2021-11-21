'''
Given strings a and b, and an integer k, return whether a can be converted to b by shifting some characters clockwise at most k times.

For example, "c" can be turned into "e" using 2 clockwise shifts.
'''

# Binary Search - Your code took 23 milliseconds — faster than 57.96% in Python.

def string_clockwise_shift(a, b, k):
    for char_a, char_b in zip(a, b):
        if ord(char_b) - ord(char_a) >= 0:
            k -= (ord(char_b) - ord(char_a))
        elif ord(char_b) - ord(char_a) < 0:
            k -= 26 + (ord(char_b) - ord(char_a))
        if k < 0:
            return False
    return True
