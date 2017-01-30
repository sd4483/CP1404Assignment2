# create your BookList class in this file
import csv
from book import Book

class BookList:

    def __init__(self,booklists=[]):
        self.booklists = booklists

    def __str__(self):
        for book in self.booklists:
            print(book)
        return("end of list")

    def add_book(self,newbook):

        self.booklists.append(newbook)

    def listbooks(self):

        mybooks = open("books.csv", 'r')
        for index, data in enumerate(mybooks.readlines()):
            data = data.strip()
            datum = data.split(",")

            tempbook = Book(datum[0],datum[1],datum[2],datum[3])
        self.booklists.append(tempbook)

    def list_req_books(self):
        for each in self.booklists:
            if each.status == "r":
                print(each)

    def list_com_books(self):
        for each in self.booklists:
            if each.status == "c":
                print(each)


