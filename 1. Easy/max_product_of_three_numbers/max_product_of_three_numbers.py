'''
Given a list of integers nums, find the largest product of three distinct elements.
'''

# Binary Search - Your code took 53 milliseconds — faster than 21.11% in Python.

import heapq
import math

def max_product_of_three_numbers(nums):
        if len(nums) == 3:
            return math.prod(nums)
        largest = heapq.nlargest(3, nums)
        smallest = heapq.nsmallest(3, nums)
        product_pos = largest[0] * largest[1] * largest[2]
        if smallest[0] < 0 and smallest[1] < 0:
            product_neg = smallest[0] * smallest[1]
        else:
            product_neg = 0
        if product_pos > largest[0] * product_neg:
            return product_pos
        return largest[0] * product_neg