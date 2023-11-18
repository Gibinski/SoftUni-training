from  abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter(ABC):
    def format(self, book: Book) -> str:
        return book.content


class PressFormatter:
    def format(self, book: Book) -> str:
        return book.content[:20]
        

class EmailFormater:
    def format(self, book: Book) -> str:
        return book.content[:20]


class Printer:
    def get_book(self, book: Book):
        formatted_book = formatter.format(book)
        return formatted_book
    

formatter = Formatter()