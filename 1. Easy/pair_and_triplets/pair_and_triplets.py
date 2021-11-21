'''
You are given a string s containing digits from 0 to 9. 

Return whether there is some arrangement where we can have one pair of the same digits and the rest of the numbers form any number of triples of the same digits.
'''

# Binary Search - Your code took 49 milliseconds — faster than 19.21% in Python.

from collections import Counter

def pair_and_triplets(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    pair = 0
    triplet = 0
    for k in d:
        if d[k] == 2:
            pair += 1
            if pair > 1:
                return False
        elif (d[k] - 2) % 3 == 0:
            pair += 1
            triplet += 1
        elif d[k] % 3 != 0:
            return False
    if pair != 1:
        return False
    else:
        return True