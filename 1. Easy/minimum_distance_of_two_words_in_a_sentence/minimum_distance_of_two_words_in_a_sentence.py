'''
Given the strings text, word0, and word1, return the smallest distance between any two occurrences of word0 and word1 in text, measured in number of words. 

If either word0 or word1 doesn't appear in text, return -1.
'''
# Binary Search - Your code took 79 milliseconds — faster than 39.86% in Python.

def minimum_distance_of_two_words_in_a_sentence(text, word0, word1):
    if not word0 in text or not word1 in text:
        return -1
    list_words = text.split()
    sorted_list = []
    difference = len(list_words)-1
    for idx, word in enumerate(list_words):
        if word == word0 or word == word1:
            sorted_list.append((idx, word))
        if len(sorted_list) > 1 and sorted_list[-1][1] != sorted_list[-2][1] and abs(sorted_list[-1][0] - sorted_list[-2][0]) < difference:
            difference = abs(sorted_list[-1][0] - sorted_list[-2][0])-1
    return difference