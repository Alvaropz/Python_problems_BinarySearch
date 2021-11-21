'''
Given a string s, consisting of digits and lowercase alphabet characters, that's a run-length encoded string, return its decoded version.

Note: The original string is guaranteed not to have numbers in it.
'''

# Binary Search - Your code took 2 milliseconds — faster than 100.00% in Python.

def run_length_decoding(s):
    new_string = ""
    temp_multiplier = ""
    for index in range(len(s)):
        if s[index].isdigit():
            temp_multiplier += s[index]
        else:
            new_string += s[index] * int(temp_multiplier)
            temp_multiplier = ""
    return new_string