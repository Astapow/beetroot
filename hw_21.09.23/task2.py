class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: object):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author: object):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f'Library->{self.name}'

    def __str__(self):
        return f'Library: {self.name}'


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.total_books += 1

    def __repr__(self):
        return f'Book ->{self.name}, {self.year}, {self.author}'

    def __str__(self):
        return f'Book {self.name} {self.year}'


class Author:

    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f'Author->{self.name}, {self.country}, {self.birthday}'

    def __str__(self):
        return f'Author: {self.name}'


library = Library("My Library")
author1 = Author("SSS", "UK", "06.09.1965")
author2 = Author("GGG", "UK", "23.01.1903")
author3 = Author("KKK", "UA", "16.05.1999")

book1 = library.new_book("Tom Harry", 1997, author1)
book2 = library.new_book("Tom", 1949, author2)
book3 = library.new_book("Kelly", 2018, author3)

print(book1)
print(book2)
print(library.group_by_author(author2))
print(library.group_by_author(author1))
print(library.group_by_author(author3))
print(library.group_by_year(1997))
print(library.group_by_year(1949))
print(Book.total_books)
