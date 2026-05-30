"""Homework 21: library"""


class Book:
    """Class Book"""

    def __init__(self, book_name, author, num_pages, isbn):
        """Constructor class Book"""
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.available = True
        self.is_reserved = None
        self.is_took = None

    def reserve(self, reader):
        """Book reservation"""
        if self.is_reserved is not None:
            print("You cannot reserve the book (it's already reserved)")
            return False
        if not self.available:
            print("The book has been issued but cannot be reserved.")
            return False
        self.is_reserved = reader
        print(f"Book reserved by {reader.name}")
        return True

    def cancel_reserve(self, reader):
        """Cancelling a book reservation"""
        if self.is_reserved != reader:
            print("Not his reservation")
            return False
        self.is_reserved = None
        print("Reservation canceled")
        return True

    def get_book(self, reader):
        """Giving out a book to someone else"""
        if not self.available:
            print("The book has already been issued")
            return False
        if self.is_reserved is not None and self.is_reserved != reader:
            print("The book is reserved for someone else")
            return False
        self.available = False
        self.is_took = reader
        if self.is_reserved == reader:
            self.is_reserved = None
        print(f"{reader.name} took the book")
        return True

    def return_book(self, reader):
        """Returning a book to the library"""
        if self.is_took != reader:
            print("Another person took it")
            return False
        self.available = True
        self.is_took = None
        print(f"{reader.name} returned the book")
        return True


class Reader:
    """Class Reader"""

    def __init__(self, name):
        """Constructor class Reader"""
        self.name = name

    def reserve_book(self, book_):
        """Reserve a book"""
        return book_.reserve(self)

    def cancel_reserve(self, book_):
        """Cancel a book"""
        return book_.cancel_reserve(self)

    def get_book(self, book_):
        """Take a book"""
        return book_.get_book(self)

    def return_book(self, book_):
        """Return the book"""
        return book_.return_book(self)
