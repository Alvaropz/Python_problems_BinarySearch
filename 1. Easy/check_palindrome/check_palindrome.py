'''
Given a string s, return whether it is a palindrome. A palindrome is when the word is the same forwards and backwards.

For example, "tacocat" is a palindrome.
'''

#Binary Search - Your code took 1 millisecond — faster than 99.94% in Python

def check_palindrome_optimised(s):
    if s == s[::-1]:
        return True
    return False
    
# Binary Search - Your code took 2 milliseconds — faster than 10.95% in Python

def check_palindrome_slow(s):
    reversed_s_list = [char for char in s]
    reversed_s_list.reverse()
    reversed_string = ""
    for char in reversed_s_list:
        reversed_string += char
    if reversed_string == s:
        return True
    return False