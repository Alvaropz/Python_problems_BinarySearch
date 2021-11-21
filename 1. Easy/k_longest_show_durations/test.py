import unittest

from k_longest_show_durations import k_longest_show_durations

class TestCases(unittest.TestCase):
    def test_k_longest_show_durations(self):
        self.assertEqual(k_longest_show_durations(["Top Gun","Aviator","Top Gun","Roma","Logan"], [5,3,5,13,4], 2), 23)
        self.assertEqual(k_longest_show_durations(["Top Gun","Aviator","Top Gun","Roma","Logan"], [2,1,5,13,17], 2), 30)
        self.assertEqual(k_longest_show_durations(["Aviator","Top Gun","Roma"], [3,5,13], 2), 18)
        self.assertEqual(k_longest_show_durations(["Harry Potter", "The Lord of the Rings", "Harry Potter", "Star wars", "Harry Potter"], [17,21,8,56,11], 2), 92)
        self.assertEqual(k_longest_show_durations(["The Tunnel"], [4], 1), 4)

if __name__ == "__main__":
    unittest.main(verbosity=2)