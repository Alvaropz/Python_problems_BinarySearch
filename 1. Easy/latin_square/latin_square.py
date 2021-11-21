'''
Given an N by N matrix of letters matrix, return whether there are exactly N different letters that appear in the matrix and each letter appears exactly once in each row and exactly once in each column.
'''
#Binary Search - Your code took 1 millisecond — faster than 100.00% in Python

from collections import Counter

def latin_square(matrix):
    dict_ref = Counter(matrix[0])
    for sub_list in matrix:
        dict_counter = Counter(sub_list)
        if dict_ref != dict_counter:
            return False
    for el_indx in range(len(matrix)):
        dict_counter = {}
        for list_indx in range(len(matrix)):
            current_element = matrix[list_indx][el_indx]
            if not current_element in dict_counter:
                dict_counter[current_element] = 1
            else:
                dict_counter[current_element] += 1
        if dict_ref != dict_counter:
            return False
    return True
