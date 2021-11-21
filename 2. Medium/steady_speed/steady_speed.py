'''
You are given a list of integers positions representing the position of a car at equally spaced intervals of time. 

Return the length of the longest sublist where the car was traveling at a constant speed.

Input: positions = [0, 3, 6, 5, 4, 3, 1, 7, 10, 13]
Ouput: 4
The longest period the car was traveling at a constant speed was in the sublist [6, 5, 4, 3]
'''

# Binary Search - Your code took 534 milliseconds — faster than 7.00% in Python.

def steady_speed(positions):
    longest = 0
    for i in range(1, len(positions)):
        abs_difference = abs(positions[i] - positions[i-1])
        temp_longest = 1
        for i_sublist in range(i, len(positions)):
            if abs(positions[i_sublist] - positions[i_sublist - 1]) == abs_difference:
                temp_longest += 1
            else:
                break
        if temp_longest > longest:
            longest = temp_longest
        if longest > len(positions) - i:
            break
    return longest