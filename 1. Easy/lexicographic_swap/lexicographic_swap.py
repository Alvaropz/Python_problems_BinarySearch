'''
Given a string s, return the lexicographically smallest string that can be made if you can make at most one swap between two characters in the string.
'''

# Binary Search - Your code took 6 milliseconds — faster than 97.42% in Python.

def lexicographic_swap(s):
    if len(s) > 1:
        min_index = len(s) - s[::-1].index(min(s)) - 1
        min_char = min(s)
        for idx, char in enumerate(s):
            if idx+1 == min_index:
                return s[:idx] + min_char + char + s[min_index+1:]
            if char > min_char and idx < min_index and min_index < len(s)-1:
                return s[:idx] + min_char + s[idx+1:min_index] + char + s[min_index+1:]
            if char > min_char and idx < min_index:
                return s[:idx] + min_char + s[idx+1:min_index] + char
    return s