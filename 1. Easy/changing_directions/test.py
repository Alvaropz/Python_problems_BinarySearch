import unittest

from changing_directions import changing_directions

class TestCases(unittest.TestCase):
    def test_changing_directions(self):
        self.assertEqual(changing_directions([1,3,9,7,5,10,12]), 2)
        self.assertEqual(changing_directions([1,2,3,3,2,1]), 0)
        self.assertEqual(changing_directions([1,3,9,7,5,10,12,11]), 3)
        self.assertEqual(changing_directions([1,3,9,7,5,10,12,11,15,17,21]), 4)
        self.assertEqual(changing_directions([1,3,4,5,9,11,15]), 0)
        self.assertEqual(changing_directions([6,5,4,3,2,1]), 0)
        self.assertEqual(changing_directions([]), 0)
        self.assertEqual(changing_directions([1,2,1,2,1,2,1,2,1]), 7)

if __name__ == "__main__":
    unittest.main(verbosity=2)