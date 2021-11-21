'''
You are given an integer n consisting of digits 1, 2, and 3 and you can flip one digit to a 3. Return the maximum number you can make.
'''

# Binary Search - Your code took 1 millisecond — faster than 99.83% in Python

def number_flip_123(n):
    n_string = str(n)
    for index, number in enumerate(n_string):
        int_number = int(number)
        if int_number < 3:
            return int(n_string[:index] + "3" + n_string[index+1:])
    return int(n_string)