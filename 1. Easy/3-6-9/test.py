import unittest

from three_six_nine import three_six_nine, three_six_nine_optimised

class TestCases(unittest.TestCase):
    def test_three_six_nine(self):
        self.assertEqual(three_six_nine(1), ['1'])
        self.assertEqual(three_six_nine(3), ['1', '2', 'clap'])
        self.assertEqual(three_six_nine(4), ['1', '2', 'clap', '4'])
        self.assertEqual(three_six_nine(5), ['1', '2', 'clap', '4', '5'])
        self.assertEqual(three_six_nine(6), ['1', '2', 'clap', '4', '5', 'clap'])
        self.assertEqual(three_six_nine(12), ['1', '2', 'clap', '4', '5', 'clap', '7', '8', 'clap', '10', '11', 'clap'])
    
    def test_three_six_nine_optimised(self):
        self.assertEqual(three_six_nine_optimised(1), ['1'])
        self.assertEqual(three_six_nine_optimised(3), ['1', '2', 'clap'])
        self.assertEqual(three_six_nine_optimised(4), ['1', '2', 'clap', '4'])
        self.assertEqual(three_six_nine_optimised(5), ['1', '2', 'clap', '4', '5'])
        self.assertEqual(three_six_nine_optimised(6), ['1', '2', 'clap', '4', '5', 'clap'])
        self.assertEqual(three_six_nine_optimised(12), ['1', '2', 'clap', '4', '5', 'clap', '7', '8', 'clap', '10', '11', 'clap'])

if __name__ == "__main__":
    unittest.main(verbosity=2)