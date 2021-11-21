'''
Given a list of strings words, concatenate the strings in camel case format.
'''

# Binary Search - Your code took 9 milliseconds — faster than 85.91% in Python.

def camel_case(words):
    words = [words[index].lower().capitalize() for index in range(len(words))]
    words[0] = words[0].lower()
    return "".join(words)