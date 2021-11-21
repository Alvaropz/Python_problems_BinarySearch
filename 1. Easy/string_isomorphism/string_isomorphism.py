'''
Given lowercase alphabet strings s, and t return whether you can create a 1-to-1 mapping for each letter in s to another letter (could be the same letter) such that s could be mapped to t, with the ordering of characters preserved.
'''

# Binary Search - Your code took 2 milliseconds — faster than 33.13% in Python.

def string_isomorphism(s, t):
    dict_letters_s = {}
    dict_letters_t = {}
    for idx, (letter1,letter2) in enumerate(zip(s, t)):
        if letter1 in dict_letters_s:
            dict_letters_s[letter1].append(t[idx])
        else:
            dict_letters_s[letter1] = [t[idx]]
        if letter2 in dict_letters_t:
            dict_letters_t[letter2].append(s[idx])
        else:
            dict_letters_t[letter2] = [s[idx]]
    for k_s, k_t in zip(dict_letters_s, dict_letters_t):
        if len(list(dict.fromkeys(dict_letters_s[k_s]))) > 1:
            return False
        if len(list(dict.fromkeys(dict_letters_t[k_t]))) > 1:
            return False
    return True