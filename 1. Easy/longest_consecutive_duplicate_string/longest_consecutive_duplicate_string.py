'''
Given a string s, return the length of the longest substring with same characters.
'''

# Binary Search - Your code took 2 milliseconds — faster than 90.03% in Python

def longest_consecutive_duplicate_string(s):
    if len(s) != 0:
        count = 0
        for index, element in enumerate(s):
            next_index = index + 1
            temp_count = 1
            if index != len(s)-1:
                while element == s[next_index]:
                    temp_count += 1
                    if count < temp_count:
                        count = temp_count
                    next_index += 1
                    if next_index == len(s):
                        break
        return count
    else:
        return 0