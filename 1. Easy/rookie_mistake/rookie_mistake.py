'''
You’re given a string s containing letters of three types, R, B, and ..

R represents your current position, B represents a blocked position, and . represents an empty position. In one step, you can move to any adjacent position to your current position, as long as it is empty. Can you reach either the leftmost position or the rightmost position?

Return true if you can reach either the leftmost or the rightmost position, or false if you cannot.
'''

#Binary Search - Your code took 9 milliseconds — faster than 90.77% in Python

def rookie_mistake(s):
    if "R" in s:
        index_R = s.index("R")
    if "B" in s[:index_R] and "B" in s[index_R+1:]:
        return False
    return True