'''
Given two strings s0 and s1, determine if one is a rotation of the other.
'''

# Binary Search: Your code took 103 milliseconds — faster than 14.05% in Python

def rotation_of_another_string(s0, s1):
    if s0 == s1:
        return True
    if len(s0) != len(s1):
        return False
    new_s = ""
    starting_chars = s0[0] + s0[1]
    finishing_chars = s0[-2] + s0[-1]
    for index, char in enumerate(s1):
        if index+1 != len(s1):
            if s1[index-2] + s1[index-1] + char + s1[index+1] == finishing_chars + starting_chars:
                try:
                    if s1[index-3] == s0[-3] and s1[index+2] == s0[2]:
                        new_s = s1[index:] + s1[:index]
                        break
                except:
                    new_s = s1[index:] + s1[:index]
                    break
        else:
            if char + s1[0] == starting_chars:
                new_s = s1[index:] + s1[:index]
                break
    if s0 == new_s:
        return True
    return False