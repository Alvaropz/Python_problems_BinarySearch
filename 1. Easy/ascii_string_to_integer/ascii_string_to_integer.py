'''
You are given a string s containing digits from "0" to "9" and lowercase alphabet characters. Return the sum of the numbers found in s.
'''

# Binary Search - Your code took 92 milliseconds — faster than 9.68% in Python.

def ascii_string_to_integer(s):
    temp_string = ""
    number_list = []
    for idx in range(len(s)):
        if s[idx].isdigit():
            temp_string += s[idx]
        if s[idx].isalpha() and temp_string != "" or (idx == len(s)-1 and temp_string != ""):
            number_list.append(int(temp_string))
            temp_string = ""
    return sum(number_list)