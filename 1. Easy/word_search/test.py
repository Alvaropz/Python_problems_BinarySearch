import unittest

from word_search import word_search

class TestCases(unittest.TestCase):
    def test_word_search(self):
        self.assertEqual(word_search([["A", "B", "C", "D", "E"],["H", "E", "U", "L", "O"]], "U"), True)
        self.assertEqual(word_search([["A", "B", "C", "D", "E"],["H", "E", "K", "J", "O"]], "KJ"), True)
        self.assertEqual(word_search([["A", "B", "C", "D", "E"],["H", "E", "L", "L", "O"]], "HELLO"), True)
        self.assertEqual(word_search([["A", "B", "C", "D", "E"],["H", "E", "L", "L", "O"]], "HELLA"), False)
        self.assertEqual(word_search([["A", "B", "C", "D", "E"],["H", "E", "L", "L", "O"]], "HEYLA"), False)
        self.assertEqual(word_search([['F', 'A', 'F'],['O', 'B', 'Q'],['A', 'X', 'O'],['M', 'A', 'B']], "FOAM"), True)
        self.assertEqual(word_search([['A', 'F', 'C'],['B', 'O', 'Q'],['X', 'A', 'O'],['A', 'M', 'B']], "FOAM"), True)
        self.assertEqual(word_search([['A', 'C', 'F'],['B', 'Q', 'O'],['X', 'A', 'O'],['A', 'M', 'B']], "FOAM"), False)
        self.assertEqual(word_search([['A', 'C', 'F'],['B', 'N', 'A'],['X', 'O', 'O'],['A', 'M', 'B']], "NO"), True)
        self.assertEqual(word_search([['A', 'C', 'F'],['B', 'X', 'N'],['X', 'X', 'O'],['A', 'M', 'B']], "NO"), True)
        self.assertEqual(word_search([['A', 'C', 'F'],['B', 'X', 'A'],['N', 'X', 'O'],['O', 'M', 'B']], "NO"), True)
        self.assertEqual(word_search([["x", "z", "d", "x"],["p", "g", "u", "x"],["k", "j", "z", "d"]], "dxx"), False)    

if __name__ == "__main__":
    unittest.main(verbosity=2)