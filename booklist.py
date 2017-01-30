# create your BookList class in this file

from book import Book
from operator import attrgetter

class BookList:

    def __init__(self):
        booklists = []
        self.booklists = booklists

    def __getitem__(self, item):
        return self.booklists[item]

    def __str__(self):
        return self.booklists

    def add_book(self,title,author,pages):
        newbook = Book(title,author,pages,'r')
        self.booklists.append(newbook)

    def listbooks(self):

        file_pointer = open("books.csv", 'r')
        for index, data in enumerate(file_pointer.readlines()):
            data = data.strip()
            datum = data.split(",")
            list_book = Book(datum[0],datum[1],datum[2], datum[3])
            self.booklists.append(list_book)
        file_pointer.close()
        return self.booklists

    def sort_books(self):
        sort = self.booklists.sort(key=attrgetter('author', 'pages'))
        return sort

    def save_books(self):
        writer = open("books.csv", "w")
        for each in range(len(self.booklists)):
            item = self.booklists[each]
            each = "{},{},{},{}\n" .format(item.title,item.author,item.pages,item.status)
            writer.write(each)
        writer.close()

    def requiredbooks_pages(self):
        req_books_pages = 0
        for i in range(len(self.booklists)):
            if self.booklists[i].status == 'r':
                count_pages = self.booklists[i].pages
                req_books_pages += (int(count_pages))
        total_req_book_pages = "Total pages to read: {}" .format(req_books_pages)
        return total_req_book_pages

    def completedbooks_pages(self):
        com_books_pages = 0
        for i in range(len(self.booklists)):
            if self.booklists[i].status == 'c':
                count_pages = self.booklists[i].pages
                com_books_pages += (int(count_pages))
        total_com_book_pages = "Total pages complete: {}" .format(com_books_pages)
        return total_com_book_pages

    def extraPages(self,pages):
        if int(pages) > 500:
            return True
        else:
            return False


