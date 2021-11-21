'''
Given positive integers start and end (start < end), return the minimum number of operations needed to convert start to end using these operations:

Increment by 1
Multiply by 2
'''

# Binary Search - Your code took 2 milliseconds — faster than 36.14% in Python.

def target_number_with_operations(start, end):
    operations = 0
    while end > start:
        new_end = int(end/2)
        if end % 2 == 0 and new_end >= start:
            end = new_end
        elif end % 2 == 0 and new_end < start:
            operations += (end-start)
            return operations
        else:
            end -= 1
        operations += 1
        if end == start:
            return operations