'''
Given a string s consisting only of 1s and 0s, you can delete any two adjacent letters if they are different.

Return the length of the smallest string that you can make if you're able to perform this operation as many times as you want.
'''


# Binary Search - Your code took 49 milliseconds — faster than 47.82% in Python

def shortest_string(s):
    copied_string = s
    while True:
        if "01" in s:
            copied_string =  copied_string.replace("01", "")
        if "10" in s:
            copied_string =  copied_string.replace("10", "")
        if not "10" in copied_string and not "01" in copied_string:
            break
        if len(copied_string) == 2 and ("10" in copied_string or "01" in copied_string):
            return 0
    return len(copied_string)