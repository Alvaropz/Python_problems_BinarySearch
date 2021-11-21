'''
Given a two-dimensional square matrix, rotate in-place it 90 degrees counter-clockwise.
'''

# Binary Search - Your code took 9 milliseconds — faster than 76.80% in Python.

def rotate_by_ninety_degrees_counter_clockwise_append(matrix):
    final_list = []
    for r in range(len(matrix)):
        temp_list = []
        for c in range(len(matrix[r])):
            temp_list.append(matrix[c][r])
        final_list.append(temp_list)
    return final_list[::-1]

def rotate_by_ninety_degrees_counter_clockwise_insert(matrix):
    final_list = []
    for r in range(len(matrix)):
        temp_list = []
        for c in range(len(matrix[r])):
            temp_list.append(matrix[c][r])
        final_list.insert(0,temp_list)
    return final_list