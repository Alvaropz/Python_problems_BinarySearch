'''
Given a list of strings book, page an index (0-indexed) into the book, and page_size, return the list of words on that page.

If the page is out of index, return an empty list.
'''

# Binary Search - Your code took 2 milliseconds — faster than 33.07% in Python.

def book_pagination(book, page, page_size):
    if page_size == 0:
        return []
    list_book = []
    total_pages = int(len(book) / page_size)
    if page > total_pages:
        return []
    location = 0
    while location < total_pages+1:
        list_book.append(book[0:page_size])
        del book[:page_size]
        location += 1
    return list_book[page]


# Binary Search - Your code took 1 milliseconds — faster than 100.00% in Python.

def book_pagination_optimised(book, page, page_size):
        if page_size == 0:
            return []
        total_pages = int(len(book) / page_size)
        if page > total_pages:
            return []
        index_ref = page_size*page
        return book[index_ref:index_ref+page_size]