class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page



class Library:
    """
        Class Library
    """
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, title: str):
        try:
            book = [b for b in self.books if b.title == title]
            return book
        except IndexError:
            return None
        

book1 = Book("Title1", "Autor1")
book2 = Book("Title2", "Autor2")

library = Library()
library.add_book(book1)
print(library.books)