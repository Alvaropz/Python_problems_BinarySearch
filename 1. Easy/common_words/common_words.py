'''
Given two strings s0 and s1, each representing a sentence, return the number of unique words that are shared between the two sentences.

Note: words are case-insensitive so "hello" and "Hello" are the same word.
'''

# Binary Search - Your code took 71 milliseconds — faster than 31.95% in Python

def common_words(s0, s1):
    list_s0 = list(set(s0.lower().split()))
    set_s1 = set(s1.lower().split())
    total_count = 0
    for word in list_s0:
        if word in set_s1:
            total_count += 1
    return total_count
