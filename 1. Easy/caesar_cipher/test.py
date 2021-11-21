import unittest

from caesar_cipher import cipher_slow, cipher_faster

class StringTest(unittest.TestCase):
    def test_slow(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        k = 4
        self.assertEqual(cipher_slow(s, k), "efghijklmnopqrstuvwxyzabcd")
        k = -4
        self.assertEqual(cipher_slow(s, k), "wxyzabcdefghijklmnopqrstuv")
        s = "zzzisnotthesameasyyy"
        k = 1
        self.assertEqual(cipher_slow(s, k), "aaajtopuuiftbnfbtzzz")
        s = "thisisacriptedmessageinenglish"
        k = -468
        self.assertEqual(cipher_slow(s, k), "thisisacriptedmessageinenglish")
        s = "esteesunmensajecifradoenespanol"
        k = 1962
        self.assertEqual(cipher_slow(s, k), "qefqqegzyqzemvqourdmpaqzqebmzax")

    def test_faster(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        k = 4
        self.assertEqual(cipher_faster(s, k), "efghijklmnopqrstuvwxyzabcd")
        k = -4
        self.assertEqual(cipher_faster(s, k), "wxyzabcdefghijklmnopqrstuv")
        s = "zzzisnotthesameasyyy"
        k = 1
        self.assertEqual(cipher_faster(s, k), "aaajtopuuiftbnfbtzzz")
        s = "thisisacriptedmessageinenglish"
        k = -468
        self.assertEqual(cipher_faster(s, k), "thisisacriptedmessageinenglish")
        s = "esteesunmensajecifradoenespanol"
        k = 1962
        self.assertEqual(cipher_faster(s, k), "qefqqegzyqzemvqourdmpaqzqebmzax")

if __name__ == "__main__":
    unittest.main(verbosity=2)