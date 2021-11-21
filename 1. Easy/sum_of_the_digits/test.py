import unittest

from sum_of_the_digits import sum_of_the_digits

class TestCases(unittest.TestCase):
    def test_sum_of_the_digits(self):
        self.assertEqual(sum_of_the_digits(938897), 44)
        self.assertEqual(sum_of_the_digits(123), 6)
        self.assertEqual(sum_of_the_digits(94785357963218098690), 109)
        
if __name__ == "__main__":
    unittest.main(verbosity=2)