import unittest

from book_pagination import book_pagination, book_pagination_optimised

class TestCases(unittest.TestCase):
    def test_book_pagination(self):
        book = ["concrete", "genuine", "plaster", "compact", "operation", "truth", "west"]
        page = 1
        page_size = 3
        self.assertEqual(book_pagination(book, page, page_size), ["compact", "operation", "truth"])
        book = ["concrete", "genuine", "plaster", "compact", "operation", "truth", "west"]
        page = 1
        page_size = 0
        self.assertEqual(book_pagination(book, page, page_size), [])
        book = ["concrete", "genuine", "plaster", "compact", "operation", "truth", "west"]
        page = 5
        page_size = 3
        self.assertEqual(book_pagination(book, page, page_size), [])
        book = ["concrete", "genuine", "plaster", "compact", "operation", "truth", "west"]
        page = 1
        page_size = 3
        self.assertEqual(book_pagination(book, page, page_size), ["compact", "operation", "truth"])
        book = ["concrete", "genuine", "plaster", "compact", "operation", "truth", "west"]
        page = 1
        page_size = 0
        self.assertEqual(book_pagination(book, page, page_size), [])
        book = ["concrete", "genuine", "plaster", "compact", "operation", "truth", "west"]
        page = 0
        page_size = 2
        self.assertEqual(book_pagination(book, page, page_size), ["concrete", "genuine"])

    def test_book_pagination_optimised(self):
        book = ["concrete", "genuine", "plaster", "compact", "operation", "truth", "west"]
        page = 1
        page_size = 3
        self.assertEqual(book_pagination_optimised(book, page, page_size), ["compact", "operation", "truth"])
        book = ["concrete", "genuine", "plaster", "compact", "operation", "truth", "west"]
        page = 1
        page_size = 0
        self.assertEqual(book_pagination_optimised(book, page, page_size), [])
        book = ["concrete", "genuine", "plaster", "compact", "operation", "truth", "west"]
        page = 5
        page_size = 3
        self.assertEqual(book_pagination_optimised(book, page, page_size), [])
        book = ["concrete", "genuine", "plaster", "compact", "operation", "truth", "west"]
        page = 1
        page_size = 3
        self.assertEqual(book_pagination_optimised(book, page, page_size), ["compact", "operation", "truth"])
        book = ["concrete", "genuine", "plaster", "compact", "operation", "truth", "west"]
        page = 1
        page_size = 0
        self.assertEqual(book_pagination_optimised(book, page, page_size), [])
        book = ["concrete", "genuine", "plaster", "compact", "operation", "truth", "west"]
        page = 0
        page_size = 2
        self.assertEqual(book_pagination_optimised(book, page, page_size), ["concrete", "genuine"])


if __name__ == "__main__":
    unittest.main(verbosity=2)