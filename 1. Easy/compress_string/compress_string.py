'''
Given a string s, eliminate consecutive duplicate characters from the string and return it.

That is, if a list contains repeated characters, they should be replaced with a single copy of the character. The order of the elements should not be changed.
'''

#Binary Search - Your code took 18 milliseconds — faster than 20.09% in Python

def compress_string(s):
    sliced_s = ""
    for index, char in enumerate(s):
        if index+1 != len(s) and char != s[index+1]:
            sliced_s +=  char
    sliced_s += s[-1]
    return sliced_s