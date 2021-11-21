'''
You are given a lowercase alphabet string text. 
Return a new string where every character in text is mapped to its reverse in the alphabet, so that a becomes z, b becomes y, c becomes x, and so on.
'''

import string

# Binary Search - Your code took 8 milliseconds — faster than 76.34% in Python

def atbash_cipher_ascii_index(text):
    new_string = ""
    for char in text:
        new_string += chr(122-(ord(char)-97)) #122 represents "z" and 97 represents "a" in ascii code.
    return new_string

# Your code took 56 milliseconds — faster than 3.54% in Python

def atbash_cipher_alphabet_lists_iteration(text):
    alphabet = list(string.ascii_lowercase)
    alphabet_reversed = list(reversed(string.ascii_lowercase))
    new_string = ""
    for char in text:
        for index, alpha_char in enumerate(alphabet):
            if char == alpha_char:
                new_string += alphabet_reversed[index]
    return new_string

# Binary Search - Your code took 16 milliseconds — faster than 24.81% in Python

def atbash_cipher_lists_accesing_index(text):
    alphabet = list(string.ascii_lowercase)
    alphabet_reversed = list(reversed(string.ascii_lowercase))
    new_string = ""
    for char in text:
        ref_index = alphabet.index(char)
        new_string += alphabet_reversed[ref_index]
    return new_string