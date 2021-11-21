'''
Given two strings s0 and s1, return the two strings interleaved, starting with s0. 
If there are leftover characters in a string they should be added to the end.
'''

#Binary Search - Your code took 7 milliseconds — faster than 96.69% in Python

def interleaved_string(s0, s1):
    formatted_s = ""
    if len(s0) == 0 or len(s1) == 0:
        if len(s0) == 0:
            return s1
        return s0
    if len(s0) == len(s1):
        for index in range(len(s0)):
            formatted_s += s0[index] + s1[index]
        return formatted_s
    if len(s0) > len(s1):
        for index in range(len(s1)):
            formatted_s += s0[index] + s1[index]
        formatted_s += s0[len(s1):]
    elif len(s1) > len(s0):
        for index in range(len(s0)):
            formatted_s += s0[index] + s1[index]
        formatted_s += s1[len(s0):]
    return formatted_s