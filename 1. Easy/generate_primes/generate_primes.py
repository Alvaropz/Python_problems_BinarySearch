'''
Given a number n, return a list of all prime numbers smaller than or equal to n in ascending order.

For example, given the number 10, return the list [2, 3, 5, 7].

Note: 1 is not a prime number.
'''
#Binary Search - Your code took 8 milliseconds — faster than 28.92% in Python

def generate_primes(n):
    prime_n_ori = []
    if n > 1:
        for number in range(n+1):
            prime_n_ori.append(number)
        prime_n_ref = prime_n_ori.copy()
        if len(prime_n_ori) > 1:
            prime_n_ori.remove(0)
            prime_n_ref.remove(0)
            for numerator in prime_n_ref:
                count = 0
                for denumerator in prime_n_ori:
                    if numerator % denumerator == 0:
                        count += 1
                        if count > 2:
                            prime_n_ori.remove(numerator)
                            break
            prime_n_ori.remove(1)
    return prime_n_ori

#Binary Search - Your code took 6 milliseconds — faster than 37.72% in Python

import math

def generate_primes_v2(n):
    primes_list = []
    if n > 1:
        copy_n = n
        while copy_n > 0:
            for number in range(2, copy_n+1):
                if copy_n % number == 0 and number != copy_n:
                    break
                if number == copy_n:
                    primes_list.append(number)
            copy_n -= 1
    primes_list.sort()
    return primes_list