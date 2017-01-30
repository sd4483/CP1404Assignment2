"""
(incomplete) Tests for BookList class
"""
from booklist import BookList
from book import Book

# test empty BookList
book_list = BookList()

assert len(book_list.booklists) == 0

# test loading books
book_list.listbooks()

assert len(book_list.booklists) > 0  # assuming CSV file is not empty


# test sorting books

# test adding a new Book

# test saving books (check CSV file manually to see results)