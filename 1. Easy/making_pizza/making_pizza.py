'''
Given a lowercase alphabet string s, return how many "pizza" strings you can create using the characters in s. 
You can use the characters in s in any order, but you can only use each character once.
'''

#Binary Search - Your code took 79 milliseconds — faster than 8.05% in Python

from collections import Counter

def making_pizza(s):
    if len(s) == 0:
        return 0
    count = 0
    chars_dict = Counter(s)
    if not all (item in chars_dict for item in ("p","i","z","a")):
        return 0
    while chars_dict.get("p") > 0 or chars_dict.get("i") > 0 or chars_dict.get("z") > 0 or chars_dict.get("a") > 0:
        if chars_dict.get("p") > 0 and chars_dict.get("i") > 0 and chars_dict.get("z") > 1 and chars_dict.get("a") > 0:
            count += 1
        chars_dict["p"] = chars_dict.get("p") - 1
        chars_dict["i"] = chars_dict.get("i") - 1
        chars_dict["z"] = chars_dict.get("z") - 2
        chars_dict["a"] = chars_dict.get("a") - 1
    return count