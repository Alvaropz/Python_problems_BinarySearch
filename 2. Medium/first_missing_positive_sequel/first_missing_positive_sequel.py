'''
Given a sorted unique integer list of size n in increasing order, find the first positive integer between [1, n+1] not in the array.
'''

# Binary Search - Your code took 19 milliseconds — faster than 57.63% in Python.

def first_missing_positive_sequel(arr):
    if 0 in arr:
        arr.remove(0)
    if len(arr) % 2 == 0:
        half_index = int(len(arr)/2)
        first_half_list = arr[:half_index]
        second_half_list = arr[half_index:]
        if len(first_half_list)-first_half_list[-1] == 0:
            if not first_half_list[-1]+1 in arr:
                return first_half_list[-1]+1
            for index, number in enumerate(second_half_list):
                if index == len(second_half_list)-1:
                    return number+1
                elif number+1 != second_half_list[index+1]:
                    return number+1
        else:
            if not 1 in arr:
                return 1
            for index, number in enumerate(first_half_list):
                if index == len(first_half_list)-1:
                    return number+1
                elif number+1 != first_half_list[index+1]:
                    return number+1
    else:
        dif = sum([number for number in range(1, len(arr)+2)]) - sum(arr)
        return dif

# Binary Search - Your code took 15 milliseconds — faster than 70.72% in Python.

def first_missing_positive_sequel_optimised(arr):
    if 0 in arr:
        arr.remove(0)
    dif = sum([number for number in range(1, len(arr)+2)]) - sum(arr)
    return dif