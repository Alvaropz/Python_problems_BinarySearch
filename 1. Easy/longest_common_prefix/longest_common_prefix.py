'''
Given a list of lowercase alphabet strings words, return the longest common prefix.
'''

# Binary Search - Your code took 336 milliseconds — faster than 9.61% in Python. Importantto note! - This code passes the BinarySearch default testcases. However, this code doesn't pass the test with the ["yet", "yell", "yeast", "yearn"] testcase.

def longest_common_prefix(words):
    shortest_word = min(words)
    i = 0
    prefix = ""
    while i < len(shortest_word):
        for idx, word in enumerate(words):
            if word[i] != shortest_word[i]:
                break
            if idx == len(words)-1:
                prefix += shortest_word[i]
        i += 1
    return prefix

# Binary Search - Your code took 381 milliseconds — faster than 6.32% in Python.

def longest_common_prefix_v2(words):
    prefix = ""
    for idx_letter in range(len(words[0])):
        for idx in range(1, len(words)):
            if idx_letter < len(words[idx]):
                if words[0][idx_letter] != words[idx][idx_letter]:
                    break
                if idx == len(words)-1:
                    prefix += words[0][idx_letter]
    return prefix