'''
Given a list of strings words and a string letters, return the length of longest string in words that can be made from letters in letters. If no word can be made, return 0.

Note that you can't reuse letters.
'''

# Binary Search - Your code took 135 milliseconds — faster than 18.62% in Python.

from collections import Counter

def word_formation(words, letters):
    max_size = 0
    for word in words:
        temp_count = 0
        temp_dict = Counter(letters)
        for char in word:
            if char in temp_dict:
                if temp_dict[char] > 0:
                    temp_count += 1
                    temp_dict[char] -= 1
                else:
                    break
            else:
                break
        if temp_count == len(word) and temp_count > max_size:
            max_size = temp_count
    return max_size