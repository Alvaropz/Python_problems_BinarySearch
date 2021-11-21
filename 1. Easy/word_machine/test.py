import unittest

from word_machine import word_machine, word_machine_v2, word_machine_optimised

class TestCases(unittest.TestCase):
    def test_word_machine(self):
        self.assertEqual(word_machine(["1", "5", "DUP", "3", "-"]), -2)
        self.assertEqual(word_machine(["+"]), -1)
        self.assertEqual(word_machine(["-" ,"+"]), -1)
        self.assertEqual(word_machine(["+" ,"1"]), -1)
        self.assertEqual(word_machine(["+" ,"0"]), -1)
        self.assertEqual(word_machine(["0"]), 0)
        self.assertEqual(word_machine(["1", "1", "-", "+"]), -1)

    def test_word_machine_v2(self):
        self.assertEqual(word_machine_v2(["1", "5", "DUP", "3", "-"]), -2)
        self.assertEqual(word_machine_v2(["+"]), -1)
        self.assertEqual(word_machine_v2(["-" ,"+"]), -1)
        self.assertEqual(word_machine_v2(["+" ,"1"]), -1)
        self.assertEqual(word_machine_v2(["+" ,"0"]), -1)
        self.assertEqual(word_machine_v2(["0"]), 0)
        self.assertEqual(word_machine_v2(["1", "1", "-", "+"]), -1)

    def test_word_machine_optimised(self):
        self.assertEqual(word_machine_optimised(["1", "5", "DUP", "3", "-"]), -2)
        self.assertEqual(word_machine_optimised(["+"]), -1)
        self.assertEqual(word_machine_optimised(["-" ,"+"]), -1)
        self.assertEqual(word_machine_optimised(["+" ,"1"]), -1)
        self.assertEqual(word_machine_optimised(["+" ,"0"]), -1)
        self.assertEqual(word_machine_optimised(["0"]), 0)
        self.assertEqual(word_machine_optimised(["1", "1", "-", "+"]), -1)

if __name__ == "__main__":
    unittest.main(verbosity=2)