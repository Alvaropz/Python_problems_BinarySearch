'''
You are given a lowercase alphabet string s, and an offset integer k. Replace every letter in s with a letter k positions further along the alphabet.

Note: If the letter overflows past a or z, it gets wrapped around the other side.
'''

#Binary Search - Your code took 42 milliseconds — faster than 85.43% in Python

def cipher_faster(s, k):
    cipher = ""
    for char in s:
        con_value = (((ord(char) - 97) + k) % 26) + 97
        cipher += chr(con_value)
    return cipher

#Binary Search - Your code took 63 milliseconds — faster than 54.53% in Python

def cipher_slow(s, k):
    cipher = ""
    for char in s:
        con_value = ord(char)
        if con_value + k > ord("z") or con_value + k < ord("a"):
            con_value = (((con_value - 97) + k) % 26) + 97
            cipher += chr(con_value )
        else:
            cipher += chr(con_value + k)
    return cipher