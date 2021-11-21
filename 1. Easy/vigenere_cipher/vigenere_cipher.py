'''
You are given a lowercase alphabet string text, and another string key. Return a new string where every letter in text[i] is moved to the right with offset key[i]. Offset is equal to key[i]'s position in the alphabet (A=0, B=1 etc.)

Note: If the letter overflows past z, it gets wrapped around the other side.
'''

# Binary Search - Your code took 14 milliseconds — faster than 70.15% in Python

def vigenere_cipher(text, key):
    alphabet = string.ascii_lowercase
    position = []
    new_string = ""
    for char in key:
        position.append(alphabet.index(char))
    for index, char in enumerate(text):
        next_char_pos_ascii = ord(char)+position[index]
        if next_char_pos_ascii <= 122:
            new_string += chr(next_char_pos_ascii)
        else:
            wrap = next_char_pos_ascii - 123
            new_string += chr(97+wrap)
    return new_string

# Binary Search - Your code took 13 milliseconds — faster than 75.10% in Python

import string

def vigenere_cipher_zip(text, key):
    alphabet = string.ascii_lowercase
    position = []
    new_string = ""
    for char in key:
        position.append(alphabet.index(char))
    for char, index in zip(text, position):
        next_char_pos_ascii = ord(char)+index
        if next_char_pos_ascii <= 122:
            new_string += chr(next_char_pos_ascii)
        else:
            wrap = next_char_pos_ascii - 123
            new_string += chr(97+wrap)
    return new_string