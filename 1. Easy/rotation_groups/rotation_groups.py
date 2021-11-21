'''
A rotation group for a string contains all of its unique rotations. For example, "123" can be rotated to "231" and "312" and they are all in the same rotation group.

Given a list of strings words, group each word by their rotation group, and return the total number of groups.
'''

# Binary Search - Your code took 9 milliseconds — faster than 76.01% in Python.
    
def rotation_groups(words):
    double_string_list = [item*2 for item in words]
    dict_counting = {}
    for word in words:
        double_ref_len = len(word)*2
        for word_reference in double_string_list:
            if word in word_reference and double_ref_len == len(word_reference):
                if not word_reference in dict_counting :
                    dict_counting[word_reference] = 1
                elif word_reference in dict_counting:
                    dict_counting[word_reference] += 1
                break
    return len(dict_counting)