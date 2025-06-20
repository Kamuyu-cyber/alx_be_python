class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book) and book not in self._books:
            self._books.append(book)
            return True
        return False

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.check_out():
                return True
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.return_book():
                return True
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")
