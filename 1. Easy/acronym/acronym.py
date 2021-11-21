'''
Given a string s representing a phrase, return its acronym. Acronyms should be capitalized and should not include the word "and".
'''

# Binary Search - Your code took 9 milliseconds — faster than 99.16% in Python.

def acronym(s):
    acronym_s = ""
    word_list = s.split()
    for word in word_list:
        if word != "and":
            acronym_s += word[0]
    return acronym_s.upper()