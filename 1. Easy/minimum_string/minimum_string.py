'''
You are given two strings s and t of equal length only consisting of lowercase letters. 

Assuming that you can first rearrange s into any order, return the minimum number of changes needed to turn s into t.
'''

# Binary Search - Your code took 21 milliseconds — faster than 93.64% in Python.

from collections import Counter

def minimum_string(s, t):
    s_dict = Counter(s)
    t_dict = Counter(t)
    for key in t_dict:
        if key in s_dict:
            if s_dict[key] - t_dict[key] < 0:
                s_dict[key] = 0
            else:
                s_dict[key] -= t_dict[key] 
    return sum(s_dict.values())