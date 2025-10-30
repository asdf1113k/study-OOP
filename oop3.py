class Book:
    def __init__(self, title:str, author:str, isbn:int, is_available: bool = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def borrow(self):
        self.is_available = False

    def return_book(self):
        self.is_available = True


class Library:
    def add_book(self, book:Book):
        print(book.title)

    def info(self):
        print(self.book)

    def info(self):
        print(self.books)

library = Library()
book1 = Book("какое-то", "кто-то", 1)
library.add_book(book1)



