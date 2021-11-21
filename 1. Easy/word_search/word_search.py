
""" Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down unidirectionally.

For example, given the following matrix:
[['F', 'A', 'C'],
 ['O', 'B', 'Q'],
 ['A', 'X', 'O'],
 ['M', 'A', 'B']]
word = "HELLO" --> True

 board = [
    ["H", "E", "L", "L", "O"],
    ["A", "B", "C", "D", "E"]
]
word = "HELLO" --> True """


#Your code took 1 millisecond — faster than 100.00% in Python

def word_search(board, word):
    for l in board:
            match = 0
            for char in l:
                if match != len(word) and char == word[match]:
                    match += 1
                    if match == len(word):
                        return True
    for index_list, l in enumerate(board):
        for index, char in enumerate(l):
            if char == word[0]:
                temp_index = index_list
                word_index = 0
                while word_index != len(word)-1:
                    word_index += 1
                    temp_index += 1
                    if temp_index < len(board):
                        if board[temp_index][index] != word[word_index]:
                            break
                        elif board[temp_index][index] == word[word_index] and word_index == len(word)-1:
                            return True
    return False