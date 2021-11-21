'''
Given a positve integer n, find the length of its Collatz sequence. 
Collatz sequence is generated sequentially where

n = n / 2 if n is even
n = 3 * n + 1 if n is odd
And the sequence ends if n = 1

'''

#Binary Search - Your code took 1 millisecond — faster than 99.93% in Python

def colltaz_f(n):
    new_list = [n]
    while n > 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int((3 * n) + 1)
        new_list.append(n)
    return len(new_list)