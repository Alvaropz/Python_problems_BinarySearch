import unittest

from line_of_people import line_of_people

class TestCases(unittest.TestCase):
    def test_line_of_people(self):
        self.assertEqual(line_of_people(10, 3, 4), 5)
        self.assertEqual(line_of_people(10, 10, 10), 0)
        self.assertEqual(line_of_people(10, 3, 10), 7)
        self.assertEqual(line_of_people(8347367, 3160029, 8291959), 5187338)
        self.assertEqual(line_of_people(1, 0, 0), 1)
        self.assertEqual(line_of_people(2, 1, 0), 1)
        self.assertEqual(line_of_people(2, 0, 1), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)