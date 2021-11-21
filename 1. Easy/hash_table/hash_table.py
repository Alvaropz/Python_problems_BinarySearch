'''
Implement a hash table with the following methods:

HashTable() constructs a new instance of a hash table
put(int key, int val) updates the hash table such that key maps to val
get(int key) returns the value associated with key. If there is no such key, then return -1.
remove(int key) removes both the key and the value associated with it in the hash table.
This should be implemented without using built-in hash table.
'''

# Binary Search - Your code took 242 milliseconds — faster than 48.88% in Python.

'''
Additional information: To create the test, I used the same method that Binary Search used to test the code. 
In this case, it's by creating an inner list, that checks the outcome for every function of the object 'HashTable'.
For instance, in Binary Search, the methods "constructor", "put" and "remove" retrieve 'none' as the value when they have been run.
Only the method "get" returns the last value of the linked list in the hash table - If the head (or reference element in the hash table) doesn't exist, it will return the value; -1.

Also, there is an additional method just for testing purposes which prints the 'hash table' once all the methods in the list have been run.

Again, this list is only needed for testing purposes. The 'hash table' itself is created by the next way:

class HashTable:
    def __init__(self):
        self.hash_table = {}

    def put(self, key, val):
        if key in self.hash_table:
            self.hash_table[key].append(val)
        else:
            self.hash_table[key] = [val]

    def get(self, key):
        if key in self.hash_table:
            return self.hash_table[key][-1]
        else:
            return -1

    def remove(self, key):
        if key in self.hash_table:
            del self.hash_table[key]
'''

class HashTable:
    def __init__(self):
        self.hash_table = {}
        self.list_arguments = [None]

    def put(self, key, val):
        if key in self.hash_table:
            self.hash_table[key].append(val)
        else:
            self.hash_table[key] = [val]
        self.list_arguments.append(None)

    def get(self, key):
        if key in self.hash_table:
            self.list_arguments.append(self.hash_table[key][-1])
            return self.hash_table[key][-1]
        else:
            self.list_arguments.append(-1)
            return -1

    def remove(self, key):
        if key in self.hash_table:
            self.list_arguments.append(None)
            del self.hash_table[key]

    def print_hash_table(self):
        return print(self.hash_table)