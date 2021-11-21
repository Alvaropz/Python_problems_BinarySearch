'''
Given a run-length encoded lowercase alphabet string s, implement an iterator which is the decoded version of s:

next() polls the next element in the iterator
hasnext() which returns whether the next element exists

Constraints:

n ≤ 100,000 where n is the number of calls to next and hasnext
'''

# Binary Search - Your code took 94 milliseconds — faster than 70.95% in Python.

class RunLengthDecodedIterator:
    def __init__(self, s):
        i = 0
        j = len(s)-1
        formated_string = ""
        while i < j:
            str_number = ""
            while s[i].isdigit():
                str_number += s[i]
                i += 1
            if int(str_number) > 100000: # This is checked just in case there is a bigger number than 100000 as number in the string. Because the constrain is that there is no more checks than 100000.
                str_number = 100000
            formated_string += (s[i]*int(str_number))
            i += 1
        self.s = formated_string
        self.i = 0

    def next(self):
        current_value = self.s[self.i]
        self.i += 1
        return current_value

    def hasnext(self):
        return self.i + 1 <= len(self.s)

