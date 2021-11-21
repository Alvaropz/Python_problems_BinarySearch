'''
Given two lowercase alphabet strings s1 and s2, determine if s1 is a subsequence of s2.
'''

# Binary Search - Your code took 33 milliseconds — faster than 59.01% in Python.

def sub_sequence_string(s1, s2):
    i_s1, i_s2 = 0, 0
    j_s1, j_s2 = len(s1)-1, len(s2)-1
    while i_s1 <= j_s1 and i_s2 <= j_s2:
        if s1[i_s1] == s2[i_s2]:
            i_s1 += 1
            i_s2 += 1
        else:
            i_s2 += 1
    if i_s1 == len(s1):
        return True
    return False
