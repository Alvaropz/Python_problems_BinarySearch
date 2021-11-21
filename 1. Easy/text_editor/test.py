import unittest

from text_editor import text_editor

class TestCases(unittest.TestCase):
    def test_text_editor(self):
        self.assertEqual(text_editor("<-"), "")
        self.assertEqual(text_editor("-<"), "-<")
        self.assertEqual(text_editor("<--"), "-")
        self.assertEqual(text_editor("<<-"), "")
        self.assertEqual(text_editor("<<<-"), "<")
        self.assertEqual(text_editor("<a<-"), "<")
        self.assertEqual(text_editor("abc<-z"), "abz")
        self.assertEqual(text_editor("<-x<-z<-"), "")

if __name__ == "__main__":
    unittest.main(verbosity=2)