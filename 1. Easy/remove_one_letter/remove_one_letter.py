'''
Given two strings s0 and s1, return whether you can obtain s1 by removing 1 letter from s0.
'''

# Binary Search - Your code took 4 milliseconds — faster than 88.70% in Python

def remove_one_letter(s0, s1):
    index = 0
    while index < len(s0):
        temp_string = s0[:index] + s0[index+1:]
        if temp_string == s1:
            return True
        index +=1
    return False