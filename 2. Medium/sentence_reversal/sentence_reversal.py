'''
Given a list of strings sentence where each sentence[i] is a string with single character, reverse the order of the words in the sentence.

You may assume there's no extraneous spaces in the sentence. Can you do modify sentence in-place and solve in \mathcal{O}(1)O(1) space?
'''

# Your code took 22 milliseconds — faster than 74.32% in Python.

def sentence_reversal_optimised(sentence):
    reversed_words_list = list(reversed("".join(sentence).split()))
    returned_list = []
    for word in reversed_words_list:
        returned_list.extend(list(word))
        returned_list.append(" ")
    returned_list.pop()
    return returned_list

# Binary Search - Your code took 102 milliseconds — faster than 34.05% in Python.

def sentence_reversal(sentence):
    i = 0
    j = len(sentence)-1
    words_list = []
    while i <= j:
        if sentence[i].isalpha():
            temp_string = ""
            while i <= j and sentence[i].isalpha():
                temp_string += sentence[i]
                i += 1
            words_list.append(temp_string)
        else:
            i += 1
    words_list = words_list[::-1]
    final_list = []
    for word in words_list:
        temp_word = list(word)
        final_list.extend(temp_word)
        final_list.append(" ")
    final_list.pop()
    return final_list