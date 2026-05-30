"""Homework 20: library"""
import unittest
from library import Book, Reader
from logger_config import get_logger

logger = get_logger(__name__)


class TestBookInit(unittest.TestCase):
    """Checking the creation of a Book instance"""

    def test_create_book_with_correct_attributes(self):
        """The book is created with the correct attributes"""
        logger.info("Test: creating a book with correct attributes")
        book = Book("The Hobbit", "J.R.R. Tolkien",
                    400, "0006754023")
        self.assertEqual(book.book_name, "The Hobbit")
        self.assertEqual(book.author, "J.R.R. Tolkien")
        self.assertEqual(book.num_pages, 400)
        self.assertEqual(book.isbn, "0006754023")
        self.assertTrue(book.available)
        self.assertIsNone(book.is_reserved)
        self.assertIsNone(book.is_took)
        logger.debug("The book has been successfully created: %s",
                     book.book_name)


class TestReserveBook(unittest.TestCase):
    """Book reserving tests"""

    def setUp(self):
        logger.info("=== Preparing reservation tests ===")
        self.book = Book("The Hobbit", "J.R.R. Tolkien",
                         400, "0006754023")
        self.vasya = Reader("Vasya")
        self.petya = Reader("Petya")
        logger.debug("Book '%s' and readers created: %s, %s",
                     self.book.book_name, self.vasya.name, self.petya.name)

    def test_reserve_available_and_not_reserved(self):
        """Successful reserving of an available book"""
        logger.debug("Test: Reserving an available book")
        result = self.book.reserve(self.vasya)
        logger.debug("Result of reserve: %s, is_reserved = %s",
                     result, self.book.is_reserved)
        self.assertTrue(result)
        self.assertEqual(self.book.is_reserved, self.vasya)
        self.assertTrue(self.book.available)

    def test_reserve_already_reserved_by_another(self):
        """You cannot reserve a book that has already been reserved"""
        logger.debug("Test: Reserving an already reserved book")
        self.book.reserve(self.vasya)
        result = self.book.reserve(self.petya)
        logger.debug("Result of re-reserving: %s", result)
        self.assertFalse(result)
        self.assertEqual(self.book.is_reserved, self.vasya)

    def test_reserve_when_book_is_taken(self):
        """You cannot reserve a book that has been issued"""
        logger.debug("Test: Reserving a book")
        self.book.get_book(self.vasya)
        result = self.book.reserve(self.petya)
        logger.debug("Result of reserving the issued book: %s", result)
        self.assertFalse(result)
        self.assertIsNone(self.book.is_reserved)


class TestCancelReserve(unittest.TestCase):
    """Cancellation Tests on reserved"""

    def setUp(self):
        logger.info("=== Preparing Cancellation Tests on reserved ===")
        self.book = Book("The Hobbit", "J.R.R. Tolkien",
                         400, "0006754023")
        self.vasya = Reader("Vasya")
        self.petya = Reader("Petya")
        logger.debug("The book and the readers are created: %s, %s",
                     self.vasya.name, self.petya.name)

    def test_cancel_own_reservation(self):
        """Reader cancels their reservation."""
        logger.debug("Test: Cancel your reservation")
        self.book.reserve(self.vasya)
        result = self.book.cancel_reserve(self.vasya)
        logger.debug("Result of cancel_reserve: %s", result)
        self.assertTrue(result)
        self.assertIsNone(self.book.is_reserved)

    def test_cancel_reservation_of_another_reader(self):
        """You can't cancel someone else's reservation"""
        logger.debug("Test: Cancelling someone else's reservation")
        self.book.reserve(self.vasya)
        result = self.book.cancel_reserve(self.petya)
        logger.debug("Result: %s, is_reserved = %s",
                     result, self.book.is_reserved)
        self.assertFalse(result)
        self.assertEqual(self.book.is_reserved, self.vasya)

    def test_cancel_when_nobody_reserved(self):
        """Cancelling a reservation when the book isn't reserved"""
        logger.debug("Test: Cancelling a reservation "
                     "when there is no reservation")
        result = self.book.cancel_reserve(self.vasya)
        logger.debug("Result: %s", result)
        self.assertFalse(result)
        self.assertIsNone(self.book.is_reserved)


class TestGetBook(unittest.TestCase):
    """Book Issue Tests"""

    def setUp(self):
        logger.info("=== Preparing book issue tests ===")
        self.book = Book("The Hobbit", "J.R.R. Tolkien",
                         400, "0006754023")
        self.vasya = Reader("Vasya")
        self.petya = Reader("Petya")

    def test_get_available_not_reserved(self):
        """Take an available unbooked book"""
        logger.debug("Test: Take an accessible book")
        result = self.book.get_book(self.vasya)
        logger.debug("Get_book result: %s, is_took = %s",
                     result, self.book.is_took)
        self.assertTrue(result)
        self.assertFalse(self.book.available)
        self.assertEqual(self.book.is_took, self.vasya)
        self.assertIsNone(self.book.is_reserved)

    def test_get_book_self_reserved(self):
        """Take a book that you reserved yourself"""
        logger.debug("Test: Take your reserved book")
        self.book.reserve(self.vasya)
        result = self.book.get_book(self.vasya)
        logger.debug("Get_book result: %s", result)
        self.assertTrue(result)
        self.assertFalse(self.book.available)
        self.assertEqual(self.book.is_took, self.vasya)
        self.assertIsNone(self.book.is_reserved)

    def test_get_book_already_taken(self):
        """You cannot take a book that has already been issued"""
        logger.debug("Test: Take a book that has already been issued")
        self.book.get_book(self.vasya)
        result = self.book.get_book(self.petya)
        logger.debug("Result: %s", result)
        self.assertFalse(result)
        self.assertFalse(self.book.available)
        self.assertEqual(self.book.is_took, self.vasya)

    def test_get_book_reserved_for_another(self):
        """You cannot take a book reserved by someone else"""
        logger.debug("Test: Take a book reserved by someone else")
        self.book.reserve(self.vasya)
        result = self.book.get_book(self.petya)
        logger.debug("Result: %s, is_took = %s", result, self.book.is_took)
        self.assertFalse(result)
        self.assertTrue(self.book.available)
        self.assertIsNone(self.book.is_took)
        self.assertEqual(self.book.is_reserved, self.vasya)


class TestReturnBook(unittest.TestCase):
    """Book return tests"""

    def setUp(self):
        logger.info("=== Preparing book return tests ===")
        self.book = Book("The Hobbit", "J.R.R. Tolkien",
                         400, "0006754023")
        self.vasya = Reader("Vasya")
        self.petya = Reader("Petya")

    def test_return_by_borrower(self):
        """Reader who took the book successfully returns it"""
        logger.debug("Test: Return of a book by the owner")
        self.book.get_book(self.vasya)
        result = self.book.return_book(self.vasya)
        logger.debug("Return_book result: %s", result)
        self.assertTrue(result)
        self.assertTrue(self.book.available)
        self.assertIsNone(self.book.is_took)

    def test_return_by_not_borrower(self):
        """Return of the book by another reader is prohibited"""
        logger.debug("Test: Attempted return by non-owner")
        self.book.get_book(self.vasya)
        result = self.book.return_book(self.petya)
        logger.debug("Result: %s", result)
        self.assertFalse(result)
        self.assertFalse(self.book.available)
        self.assertEqual(self.book.is_took, self.vasya)

    def test_return_when_not_taken(self):
        """Return of unissued book"""
        logger.debug("Test: Returning a book that was not issued")
        result = self.book.return_book(self.vasya)
        logger.debug("Result: %s", result)
        self.assertFalse(result)
        self.assertTrue(self.book.available)
        self.assertIsNone(self.book.is_took)


class TestReaderIntegration(unittest.TestCase):
    """Integration tests via Reader methods"""

    def setUp(self):
        logger.info("=== Preparing integration tests ===")
        self.book = Book("The Hobbit", "J.R.R. Tolkien",
                         400, "0006754023")
        self.vasya = Reader("Vasya")
        self.petya = Reader("Petya")

    def test_reader_reserve_and_get_own_reserved(self):
        """Vasya reserves and receives up his book"""
        logger.debug("Test: Reserving and receiving book")
        self.vasya.reserve_book(self.book)
        self.assertEqual(self.book.is_reserved, self.vasya)
        result = self.vasya.get_book(self.book)
        logger.debug("Get_book result: %s", result)
        self.assertTrue(result)
        self.assertFalse(self.book.available)
        self.assertIsNone(self.book.is_reserved)

    def test_reader_cannot_get_book_reserved_by_another(self):
        """Petya can't take the book Vasya reserved"""
        logger.debug("Test: Trying to take someone else's reservation")
        self.vasya.reserve_book(self.book)
        result = self.petya.get_book(self.book)
        logger.debug("Get_book result: %s", result)
        self.assertFalse(result)
        self.assertTrue(self.book.available)
        self.assertEqual(self.book.is_reserved, self.vasya)

    def test_reader_return_borrowed_book(self):
        """Full cycle: take – return"""
        logger.debug("Test: Complete Take-Return Cycle")
        self.vasya.get_book(self.book)
        self.assertFalse(self.book.available)
        result = self.vasya.return_book(self.book)
        logger.debug("Return_book result: %s", result)
        self.assertTrue(result)
        self.assertTrue(self.book.available)
        self.assertIsNone(self.book.is_took)

    def test_reader_cannot_return_book_taken_by_another(self):
        """Vasya can't return the book that Petya took."""
        logger.debug("Test: Trying to return someone else's book")
        self.petya.get_book(self.book)
        result = self.vasya.return_book(self.book)
        logger.debug("Return_book result: %s", result)
        self.assertFalse(result)
        self.assertEqual(self.book.is_took, self.petya)


if __name__ == '__main__':
    unittest.main()
