"""
Name: Sudheer Paturi
I.D: 13391146
Started: Jan 21
Completed: Jan 30
Github: https://github.com/sd4483/CP1404Assignment2.git

Reading List 2.0 - By Sudheer Paturi

"""

from kivy.app import App
from kivy.app import Builder
from book import Book
from booklist import BookList
from kivy.uix.button import Button

class ReadingListApp(App):
    def __init__(self, **kwargs):
        "declaring variables for class book and booklist"
        super(ReadingListApp, self).__init__(**kwargs)
        book_lists = BookList()
        book_items = Book()
        self.book_lists = book_lists
        self.book_items = book_items
        self.book_lists.listbooks()

    def build(self):
        """loading kv file"""
        self.title = "Reading List 2.0 by Sudheer Paturi"
        self.root = Builder.load_file("app.kv")
        return self.root

    def on_start(self):
        """initiates the program"""
        self.book_button(way='req')
        self.root.ids.required_book_button.state = 'down'
        self.root.ids.completed_book_button.state = 'normal'

    def on_stop(self):
        "runs after program ends"
        self.book_lists.save_books()

    def add_books(self, text_title, text_author, text_pages):
        """kivy code for add books function"""
        try:
            book_pages = int(text_pages)
            if text_title=="" or text_author=="" or text_pages=="":
                self.root.ids.description.text = "All fields must be completed"
            elif book_pages < 0:
                self.root.ids.description.text = "Pages must be positive number"
                self.root.ids.text_pages.text = ""
                self.root.ids.text_pages.value = ""
            else:
                self.book_lists.add_book(text_title,text_author,text_pages)
                self.clear_text()
                self.book_lists.sort_books()
                self.on_start()
                self.root.ids.description.text = "{} by {}, {} pages is added".format(text_title,text_author,text_pages)
        except ValueError:
            if text_title=="" or text_author=="" or text_pages=="":
                self.root.ids.description.text = "All fields must be completed"
            else:
                self.root.ids.description.text = "Please enter a valid number"
                self.root.ids.text_pages.text = ""
                self.root.ids.text_pages.value = ""

    def required_books(self, instance):
        title = instance.text
        for each in self.book_lists.booklists:
            if each.title == title:
                marking = self.book_items.mark_as_complete(each.status)
                if marking == True:
                    each.status = 'c'
                self.on_start()
                self.root.ids.description.text = "{} marked as completed".format(each.title)

    def completed_books(self,instance):
        title = instance.text
        for each in self.book_lists.booklists:
            if each.title == title:
                self.root.ids.description.text = "{} (completed)".format(each)

    def book_button(self, way):
        """book button for widget box"""
        self.clear_books()
        if way == "req":#button for required books
            for each in range(len(self.book_lists.booklists)):
                if self.book_lists[each].status == 'r':

                    temp_button = Button(text=self.book_lists[each].title)
                    temp_button.bind(on_release=self.required_books)

                    page_check = self.book_lists.extraPages(self.book_lists[each].pages)
                    #checking length of pages
                    if page_check == True:
                        temp_button.background_color = 1, 2, 1, 1
                    else:
                        temp_button.background_color = 0, 0.8, 10, 1

                    self.root.ids.box.add_widget(temp_button)

            total_required_pages = self.book_lists.requiredbooks_pages()
            self.root.ids.book_pages.text = total_required_pages
            self.root.ids.description.text = "Click book to mark them as completed"

        elif way == "com":#button for completed books
            for each in range(len(self.book_lists.booklists)):
                if self.book_lists[each].status == 'c':
                    temp_button = Button(text=self.book_lists[each].title)
                    temp_button.bind(on_release=self.completed_books)
                    temp_button.background_color = 0,1.37,1.37,1
                    self.root.ids.box.add_widget(temp_button)
            total_completed_pages = self.book_lists.completedbooks_pages()
            self.root.ids.description.text = "Click book to show the description"
            self.root.ids.book_pages.text = total_completed_pages

    def select_required_books(self):
        """runs after list required is selected"""
        self.book_button(way='req')
        self.root.ids.required_book_button.state = 'down'
        self.root.ids.completed_book_button.state = 'normal'

    def select_completed_books(self):
        """runs after list completed in selected"""
        self.book_button(way='com')
        self.root.ids.required_book_button.state = 'normal'
        self.root.ids.completed_book_button.state = 'down'

    def clear_books(self):
        """clears button"""
        self.root.ids.box.clear_widgets()

    def clear_text(self):
        """clears text in the add book fields"""
        self.root.ids.text_title.text = ""
        self.root.ids.text_author.text = ""
        self.root.ids.text_pages.text = ""


ReadingListApp().run()
