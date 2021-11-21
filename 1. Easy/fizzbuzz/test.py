import unittest

from fizzbuzz import fizzbuzz

class TestCases(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(1), ['1'])
        self.assertEqual(fizzbuzz(2), ['1', '2'])
        self.assertEqual(fizzbuzz(3), ['1', '2', 'Fizz'])
        self.assertEqual(fizzbuzz(5), ['1', '2', 'Fizz', '4', 'Buzz'])
        self.assertEqual(fizzbuzz(10),['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz'])
        self.assertEqual(fizzbuzz(14), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14'])
        self.assertEqual(fizzbuzz(19), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19'])
        self.assertEqual(fizzbuzz(30), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29', 'FizzBuzz'])

if __name__ == "__main__":
    unittest.main(verbosity=2)