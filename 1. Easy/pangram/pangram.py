'''
Given a string s, representing a sentence, return whether every letter (case-insensitive) of the alphabet is used at least once.
'''

import string

#Binary Search - Set - Your code took 8 milliseconds — faster than 54.63% in Python

def pangram(s):
    alphabet = set(string.ascii_lowercase)
    lower_s = s.lower()
    list_s = [char for char in lower_s if char in alphabet]
    for char in alphabet:
        if not char in list_s:
            return False
    return True

#Binary Search - List - Your code took 38 milliseconds — faster than 17.26% in Python

def pangram_v2(s):
    alphabet = list(string.ascii_lowercase)
    lower_s = s.lower()
    list_s = [char for char in lower_s if char in alphabet]
    for char in alphabet:
        if not char in list_s:
            return False
    return True

#Binary Search - Your code took 58 milliseconds — faster than 6.63% in Python

def pangram_v3(s):
    alphabet = list(string.ascii_lowercase)
    list_s = []
    lower_s = s.lower()
    for char in lower_s:
        if char in alphabet and not char in list_s:
            list_s.append(char)
    for char in alphabet:
        if not char in list_s:
            return False
    return True
