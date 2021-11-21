'''
You are given a string s where each character is "L" meaning you moved one unit left, "R" meaning you moved one unit right, or "?" meaning either "L" or "R".

Given you are at position 0, return the maximum possible distance you could be from 0 by replacing "?" with "L" or "R".
'''

# Binary Search - Your code took 74 milliseconds — faster than 2.07% in Python.

def furthest_from_origin_v_one(s):
    list_l = ["L" if char == "?" else char for char in s] 
    list_r = ["R" if char == "?" else char for char in s]
    total_l = 0
    total_r = 0
    for char_l, char_r in zip(list_l,list_r):
        if char_l == "L":
            total_l -= 1
        elif char_l == "R":
            total_l += 1
        if char_r == "L":
            total_r -= 1
        elif char_r == "R":
            total_r += 1
    abs_total_l = abs(total_l)
    abs_total_r = abs(total_r)
    if abs_total_l >= abs_total_r:
        return abs_total_l
    else:
        return abs_total_r

# Binary Search - Your code took 28 milliseconds — faster than 34.44% in Python.

def furthest_from_origin_v_two(s):
    total_r = 0
    total_l = 0
    for char in s:
        if char == "R":
            total_r += 1
        elif char == "L":
            total_l += 1
        else:
            total_r += 1
            total_l += 1
    if total_r >= total_l:
        return total_r-s.count("L")
    return total_l-s.count("R")

# Binary Search - Your code took 5 milliseconds — faster than 99.59% in Python.

def furthest_from_origin_optimised(s):
    only_r = s.count("R")
    only_l = s.count("L")
    only_question = s.count("?")
    total_r =  only_r+only_question
    total_l = only_l+only_question
    if total_r >= total_l:
        return total_r-only_l
    return total_l-only_r