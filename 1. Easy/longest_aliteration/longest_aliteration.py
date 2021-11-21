'''
Given a list of lowercase alphabet strings words, return the length of the longest contiguous sublist where all words share the same first letter.
'''

# Binary Search - Your code took 9 milliseconds — faster than 10.66% in Python

def longest_aliteration(words):
    if len(words) != 0:
        max_contiguous = 0
        for index, word_ref in enumerate(words):
            char = word_ref[0]
            temp_contigiuous = 1
            for new_index in range(index+1, len(words)):
                if char == words[new_index][0]:
                    temp_contigiuous += 1
                else:
                    break
            if temp_contigiuous > max_contiguous:
                max_contiguous = temp_contigiuous
        return max_contiguous
    return 0