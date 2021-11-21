'''
Given a string s, consisting of "X" and "Y"s, delete the minimum number of characters such that there's no consecutive "X" and no consecutive "Y".
'''

# Binary Search - Your code took 19 milliseconds — faster than 6.13% in Python

def consecutive_duplicates(s):
    index = 0
    while index < len(s)-1:
        if s[index] == s[index+1]:
            s = s[:index] + s[index+1:]
        else:
            index += 1
    return s