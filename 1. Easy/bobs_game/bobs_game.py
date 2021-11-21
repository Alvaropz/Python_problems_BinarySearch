'''
Bob is playing a game with himself. He gives himself a list nums. 

Each round, Bob chooses two elements of the list and replaces them with one positive integer with the same sum as the numbers he selected. Bob declares victory when all of the number in the array are even.

Return the minimum number of rounds Bob must make before he can declare victory, or return -1 if Bob can never declare victory.

2 ≤ N ≤ 100,000 where N is the length of nums.
0 ≤ nums[i] ≤ 100,000
'''

# Binary Search - Your code took 13 milliseconds — faster than 87.30% in Python.

def bobs_game(nums):
    odds = 0
    for number in nums:
        if number % 2 != 0:
            odds += 1
    if odds % 2 == 0:
        return int(odds/2)
    return -1