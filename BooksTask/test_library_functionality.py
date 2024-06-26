import unittest

from book import Book
from library import Library


class TestLibraryFunctionality(unittest.TestCase):

    def test_init_library_default_name_equal(self):
        # Arrange
        library = Library()

        # Assert
        self.assertEqual(library.filename, "library.json", "Default filename is incorrect")
        self.assertListEqual(library.books, [], "Books list should be initialized as an empty list")

    def test_init_library_custom_name(self):
        # Arrange
        library = Library("custom_name")

        # Assert
        self.assertEqual(library.filename, "custom_name", "Default filename is incorrect")
        self.assertListEqual(library.books, [], "Books list should be initialized as an empty list")

    def test_add_book_function_in(self):
        # Arrange
        library = Library()
        book = Book("Harry", "Bahaa", 2001, "Magic")

        # Act
        library.add_book(book)

        # Assert
        self.assertIn(book, library.books)

    def test_add_book_function_not_in(self):
        # Arrange
        book1 = Book("Harry", "Bahaa", 2001, "Magic")
        book2 = Book("Harry", "Bahaa", 2001, "Magic")
        library = Library()

        # Act
        library.add_book(book1)

        # Assert
        self.assertNotIn(book2, library.books)

    def test_list_books(self):
        # Arrange
        library = Library()
        book1 = Book("Harry", "Bahaa", 2001, "Magic")
        book2 = Book("Potter", "Shibel", 2001, "Fantasy")
        library.add_book(book1)
        library.add_book(book2)

        expected_list_books = [book1, book2]

        # Act
        actual_list_books = library.list_books()

        # Assert
        self.assertEqual(expected_list_books, actual_list_books)

    def test_edit_book(self):

