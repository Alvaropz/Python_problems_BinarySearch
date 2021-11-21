'''
The Connell sequence is a sequence made by:

Taking the first odd integer: 1
Taking the next two even integers 2, 4
Taking the next three odd integers 5, 7, 9
Taking the next four even integers 10, 12, 14, 16
And so on.
'''

# Binary Search - Your code took 502 milliseconds — faster than 11.76% in Python.

def connell_sequence(n):
    count = 1
    connell_list = [1]
    while count <= n:
        ref_number = connell_list[-1]+1
        connell_list.append(ref_number)
        if len(connell_list)-1 == n:
            return connell_list[-1]
        times = count
        while times > 0:
            connell_list.append(ref_number+2)
            if len(connell_list)-1 == n:
                return connell_list[-1]
            ref_number += 2
            times -= 1
        count += 1