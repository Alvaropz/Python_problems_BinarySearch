import unittest

from adding_time import adding_time

class TestCases(unittest.TestCase):
    def test_adding_time(self):
        self.assertEqual(adding_time("5:30pm", 29), "05:59pm")
        self.assertEqual(adding_time("7:00pm", 13), "07:13pm")
        self.assertEqual(adding_time("12:00pm", 0), "12:00pm")
        self.assertEqual(adding_time("12:07pm", 0), "12:07pm")
        self.assertEqual(adding_time("12:00pm", 37), "12:37pm")
        self.assertEqual(adding_time("12:00am", 0), "12:00am")
        self.assertEqual(adding_time("11:02am", 7), "11:09am")
        self.assertEqual(adding_time("12:00pm", 61), "01:01pm")
        self.assertEqual(adding_time("11:00pm", 61), "12:01am")
        self.assertEqual(adding_time("10:01am", 45674), "03:15am")
        self.assertEqual(adding_time("10:01am", 456), "05:37pm")
        self.assertEqual(adding_time("04:19pm", 0), "04:19pm")
        self.assertEqual(adding_time("17:59am", 1), "06:00pm")
        self.assertEqual(adding_time("3:46am", 1234), "12:20am")
        self.assertEqual(adding_time("11:12am", 89), "12:41pm")
        self.assertEqual(adding_time("12:01am", 720), "12:01pm")
        self.assertEqual(adding_time("12:01am", 1440), "12:01am")
        self.assertEqual(adding_time("12:01pm", 720), "12:01am")
        self.assertEqual(adding_time("12:01pm", 1440), "12:01pm")

if __name__ == "__main__":
    unittest.main(verbosity=2)