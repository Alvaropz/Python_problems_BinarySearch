'''
Given a string of words delimited by spaces, reverse the order of words. For example, given "hello there my friend", return "friend my there hello".
'''

#Binary Search - Your code took 1 millisecond — faster than 99.93% in Python

def reverse_sentence(sentence):
    reverse_s = ""
    word_l = sentence.split(" ")
    for word in reversed(word_l):
        if reverse_s == "":
            reverse_s = word
        else:
            reverse_s += " " + word
    return reverse_s