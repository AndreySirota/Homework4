"""Homework 21: test_library"""


import pytest
from source.library import Book, Reader


@pytest.fixture
def book():
    """Сreating a fresh book for each test."""
    return Book(
        book_name="The Hobbit",
        author="J.R.R. Tolkien",
        num_pages=400,
        isbn="0006754023"
    )


@pytest.fixture
def vasya():
    return Reader("Vasya")


@pytest.fixture
def petya():
    return Reader("Petya")


class TestBookInitialState:
    """Checking the initial state of the book."""
    def test_initial_state(self, book, loguru_logger):
        """Verify that a newly created book is
        available and has no reservation or active loan."""
        loguru_logger.info("Checking the initial state of the book.")
        assert book.available is True
        assert book.is_reserved is None
        assert book.is_took is None


class TestReserve:
    """Book booking tests."""
    def test_reserve_success(self, book, vasya, loguru_logger):
        """An available book can be successfully
        reserved by a reader."""
        loguru_logger.info("Reserving an available book")
        result = book.reserve(vasya)
        assert result is True
        assert book.is_reserved == vasya
        assert book.available is True

    def test_reserve_already_reserved(self, book,
                                      vasya, petya, loguru_logger):
        """Reserving a book that is already
        reserved by another reader must fail."""
        loguru_logger.info("Attempting to reserve a book "
                           "that is already reserved")
        book.reserve(vasya)
        result = book.reserve(petya)
        assert result is False
        assert book.is_reserved == vasya

    def test_reserve_when_taken(self, book, vasya, petya, loguru_logger):
        """A book that has already been borrowed cannot be reserved."""
        loguru_logger.info("Attempt to reserve a book issued")
        book.get_book(vasya)
        result = book.reserve(petya)
        assert result is False
        assert book.is_reserved is None


class TestCancelReserve:
    """Booking cancellation tests."""
    def test_cancel_reserve_success(self, book,
                                    vasya, loguru_logger):
        """A reader who made the reservation can cancel
        it successfully."""
        loguru_logger.info("Successful cancellation of "
                           "a reservation by the same reader")
        book.reserve(vasya)
        result = book.cancel_reserve(vasya)
        assert result is True
        assert book.is_reserved is None

    def test_cancel_reserve_by_other(self, book,
                                     vasya, petya, loguru_logger):
        """A reservation cannot be cancelled by a different reader."""
        loguru_logger.info("Trying to cancel someone else's reservation")
        book.reserve(vasya)
        result = book.cancel_reserve(petya)
        assert result is False
        assert book.is_reserved == vasya

    def test_cancel_reserve_when_none(self, book,
                                      vasya, loguru_logger):
        """Cancelling a reservation when no reservation
        exists must return False."""
        loguru_logger.info("Cancelling a reservation when it doesn't exist")
        result = book.cancel_reserve(vasya)
        assert result is False


class TestGetBook:
    """Tests for receiving a book in hand."""
    def test_get_available_not_reserved(self, book, vasya, loguru_logger):
        """An available, unreserved book can be borrowed by any reader."""
        loguru_logger.info("Getting an available unreserved book")
        result = book.get_book(vasya)
        assert result is True
        assert book.available is False
        assert book.is_took == vasya
        assert book.is_reserved is None

    def test_get_book_reserved_by_same_reader(self,
                                              book, vasya, loguru_logger):
        """A reader who reserved a book can successfully
         borrow it, and the reservation is cleared."""
        loguru_logger.info("Receiving a book reserved by the same reader")
        book.reserve(vasya)
        result = book.get_book(vasya)
        assert result is True
        assert book.available is False
        assert book.is_took == vasya
        assert book.is_reserved is None

    def test_get_book_reserved_by_other(self, book,
                                        vasya, petya, loguru_logger):
        """A book reserved by one reader cannot be borrowed
        by a different reader."""
        loguru_logger.info("Trying to get a book"
                           " reserved by someone else")
        book.reserve(petya)
        result = book.get_book(vasya)
        assert result is False
        assert book.available is True
        assert book.is_reserved == petya

    def test_get_book_already_taken(self, book,
                                    vasya, petya, loguru_logger):
        """A book that is already loaned out cannot
         be borrowed again."""
        loguru_logger.info("Attempting to retrieve"
                           " a book that has already been issued")
        book.get_book(vasya)
        result = book.get_book(petya)
        assert result is False
        assert book.available is False
        assert book.is_took == vasya


class TestReturnBook:
    """Book return tests."""
    def test_return_success(self, book, vasya, loguru_logger):
        """The reader who borrowed the book can return it,
        making it available again."""
        loguru_logger.info("Successful book return")
        book.get_book(vasya)
        result = book.return_book(vasya)
        assert result is True
        assert book.available is True
        assert book.is_took is None

    def test_return_by_non_taker(self, book,
                                 vasya, petya, loguru_logger):
        """A reader who did not borrow the book cannot return it."""
        loguru_logger.info("Trying to return a book "
                           "to someone other than the one who took it")
        book.get_book(vasya)
        result = book.return_book(petya)
        assert result is False
        assert book.available is False
        assert book.is_took == vasya


class TestReaderMethods:
    """Tests of Reader class methods"""
    def test_reader_reserve_book(self, book, vasya, loguru_logger):
        """Reader.reserve_book() delegates to
        Book.reserve() and returns its result."""
        loguru_logger.info("Reader.reserve_book() method")
        assert vasya.reserve_book(book) is True
        assert book.is_reserved == vasya

    def test_reader_cancel_reserve(self, book, vasya, loguru_logger):
        """Reader.cancel_reserve() cancels an existing
         reservation made by that reader."""
        loguru_logger.info("Reader.cancel_reserve() method")
        book.reserve(vasya)
        assert vasya.cancel_reserve(book) is True

    def test_reader_get_book(self, book, vasya, loguru_logger):
        """Reader.get_book() borrows the book and marks
        it as taken by the reader."""
        loguru_logger.info("Reader.get_book() method")
        assert vasya.get_book(book) is True
        assert book.is_took == vasya

    def test_reader_return_book(self, book, vasya, loguru_logger):
        """Reader.return_book() returns a borrowed
         book and makes it available."""
        loguru_logger.info("Reader.return_book() method")
        book.get_book(vasya)
        assert vasya.return_book(book) is True
        assert book.available is True


class TestIntegrationScenario:
    """Integration scenario: multiple operations with different readers."""
    def test_full_flow(self, book, vasya, petya, loguru_logger):
        """End-to-end scenario exercising reserve, cancel,
         borrow, and return across two readers."""
        loguru_logger.info("Start of full scenario")
        assert vasya.reserve_book(book) is True
        assert petya.reserve_book(book) is False
        assert vasya.cancel_reserve(book) is True
        assert petya.reserve_book(book) is True
        assert vasya.get_book(book) is False
        assert petya.get_book(book) is True
        assert vasya.get_book(book) is False
        assert petya.return_book(book) is True
        assert vasya.get_book(book) is True
        loguru_logger.info("Script completed successfully")
