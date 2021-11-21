import unittest

from frame_picture import frame_picture

class TestCases(unittest.TestCase):
    def test_frame_oicture(self):
        self.assertEqual(frame_picture(["big", "data", "is", "oil"]), '********\n* big  *\n* data *\n* is   *\n* oil  *\n********')
        self.assertEqual(frame_picture(["potato", "tomato"]), '**********\n* potato *\n* tomato *\n**********')
        self.assertEqual(frame_picture(["sql", "python", "c", "c++"]), '**********\n* sql    *\n* python *\n* c      *\n* c++    *\n**********')
        self.assertEqual(frame_picture(["Seoul", "Tokyo", "Shanghai", "Hong Kong"]), '*************\n* Seoul     *\n* Tokyo     *\n* Shanghai  *\n* Hong Kong *\n*************')

if __name__ == "__main__":
    unittest.main(verbosity=2)