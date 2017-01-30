from book import Book
from operator import attrgetter

class BookList:

    def __init__(self):
        """initializing the program"""
        booklists = [] #created an open list
        self.booklists = booklists

    def __getitem__(self, item):
        return self.booklists[item]

    def __str__(self):
        """used for testing test_booklist"""
        return self.booklists

    def add_book(self,title,author,pages):
        """to add a new book"""
        newbook = Book(title,author,pages,'r')
        self.booklists.append(newbook)

    def listbooks(self):
        """to read the csv file"""
        file_pointer = open("books.csv", 'r')
        for index, data in enumerate(file_pointer.readlines()):
            data = data.strip()
            datum = data.split(",")
            list_book = Book(datum[0],datum[1],datum[2], datum[3])
            self.booklists.append(list_book)
        file_pointer.close()
        return self.booklists

    def sort_books(self):
        """sorting based title and author"""
        sort = self.booklists.sort(key=attrgetter('author', 'pages'))
        return sort

    def save_books(self):
        """finally saves the books in csv file from booklists"""
        writer = open("books.csv", "w")
        for each in range(len(self.booklists)):
            item = self.booklists[each]
            each = "{},{},{},{}\n" .format(item.title,item.author,item.pages,item.status)
            writer.write(each)
        writer.close()

    def requiredbooks_pages(self):
        """to count number of pages to be read"""
        req_books_pages = 0
        for i in range(len(self.booklists)):
            if self.booklists[i].status == 'r':
                count_pages = self.booklists[i].pages
                req_books_pages += (int(count_pages))
        total_req_book_pages = "Total pages to read: {}" .format(req_books_pages)
        return total_req_book_pages

    def completedbooks_pages(self):
        """to count number of pages completely read"""
        com_books_pages = 0
        for i in range(len(self.booklists)):
            if self.booklists[i].status == 'c':
                count_pages = self.booklists[i].pages
                com_books_pages += (int(count_pages))
        total_com_book_pages = "Total pages complete: {}" .format(com_books_pages)
        return total_com_book_pages

    def extraPages(self,pages):
        """to check for extra pages, more than 500 or so"""
        if int(pages) > 500:
            return True
        else:
            return False


