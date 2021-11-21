'''
Given a string s containing balanced parentheses "(" and ")", split them into the maximum number of balanced groups.
'''

# Binary Search - Your code took 46 milliseconds — faster than 62.01% in Python.

def parentheses_grouping(s):
    i = 0
    j = len(s)-1
    returned_list = []
    while i <= j:
        parentheses = 1
        ref_i = i
        i += 1
        while i <= j and parentheses != 0:
            if s[i] == "(":
                parentheses += 1
            else:
                parentheses -= 1
            i += 1
        returned_list.append(s[ref_i:i])
    return returned_list