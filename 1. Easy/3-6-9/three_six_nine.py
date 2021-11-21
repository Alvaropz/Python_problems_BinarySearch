'''
Given an integer n, return a list with each number from 1 to n, except if it's a multiple of 3 or has a 3, 6, or 9 in the number, it should be the string "clap".
Note: return the number as a string.
n = 16
["1", "2", "clap", "4", "5", "clap", "7", "8", "clap", "10", "11", "clap", "clap", "14", "clap", "clap"]
'''

# Binary Search - Your code took 209 milliseconds — faster than 28.01% in Python

def three_six_nine(n):
    n_list = []
    cases = ["3", "6", "9"]
    for element in range(1,n+1):
        if element % 3 == 0 or any(item in (str(element)) for item in cases):
            n_list.append("clap")
        else:
            n_list.append(str(element))
    return n_list

# Binary Search - Your code took 94 milliseconds — faster than 95.21% in Python

def three_six_nine_optimised(n):
    n_list = []
    for element in range(1,n+1):
        str_element = str(element)
        if element % 3 == 0 or "3" in str_element or "6" in str_element or "9" in str_element:
            n_list.append("clap")
        else:
            n_list.append(str_element)
    return n_list