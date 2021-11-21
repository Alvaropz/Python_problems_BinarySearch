'''
You are given a lists of non-negative integers nums. Sort the list in ascending order by the number of 1s in binary representation for each number. 

If there are ties in the number of 1s, then break ties by their value in ascending order.
'''

# Binary Search - Your code took 1559 milliseconds — faster than 6.19% in Python.

def sort_list_by_hamming_weight(nums):
    list_binary = []
    for n in nums:
        temp_binary = 0
        ref_number = n
        while ref_number > 0:
            if ref_number%2 != 0:
                temp_binary += 1
            ref_number = int(ref_number / 2)
        list_binary.append((temp_binary, n))
    return [number[1] for number in sorted(list_binary)]