'''
Given a string s and an integer n, rearrange s into n rows so that s can be read vertically (top-down, left to right).
'''

# Binary Search - Your code took 10 milliseconds — faster than 50.15% in Python.

def vertical_cipher(s, n):
    cipher_list = []
    for index, char in enumerate(s):
        if index < n:
            string_ref = char
            index_ref = index + n
            while index_ref < len(s):
                string_ref += s[index_ref]
                index_ref += n
            cipher_list.append(string_ref)
        else:
            break
    return cipher_list