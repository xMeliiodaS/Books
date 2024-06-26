import json
import os
import tempfile
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

    def test_edit_book_true(self):
        # Arrange
        title = "Harry Potter"
        new_details = {
            "title": "Harry Potter",
            "author": "J.K. Rowling",
            "publication_year": 1998,
            "genre": "Fantasy"
        }
        book = Book("Harry Potter", "J.K. Rowling", 1998, "Fantasy")

        library = Library()
        library.add_book(book)

        # Act
        result = library.edit_book(title, new_details)

        # Assert
        self.assertTrue(result, "Expected edit_book to return True")

    def test_edit_book_false(self):
        # Arrange
        title = "Harry"
        new_details = {
            "title": "Harry Potter",
            "author": "J.K. Rowling",
            "publication_year": 1998,
            "genre": "Fantasy"
        }
        book = Book("Harry Potter", "J.K. Rowling", 1998, "Fantasy")

        library = Library()
        library.add_book(book)

        # Act
        result = library.edit_book(title, new_details)

        # Assert
        self.assertFalse(result, "Expected edit_book to return True")

    # Json file should be empty.
    def test_search_books_function(self):
        # Arrange
        library = Library()
        book1 = Book("Harry", "Bahaa", 2001, "Magic")
        book2 = Book("Potter", "Shibel", 2001, "Fantasy")
        library.add_book(book1)
        library.add_book(book2)

        expected_search_list_books = [book1]

        # Act
        query = "Harry"
        actual_search_list_books = library.search_books(query)

        # Assert
        self.assertEqual(expected_search_list_books, actual_search_list_books)

    def test_delete_function(self):
        # Arrange
        book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "Fantasy")
        book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy")
        library = Library()
        library.add_book(book1)
        library.add_book(book2)

        # Act

        # Assert

    def test_save_library_function(self):
        # Arrange
        book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "Fantasy")
        book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy")
        library = Library()
        library.add_book(book1)
        library.add_book(book2)

        # Create a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_filename = temp_file.name
        temp_file.close()

        library.filename = temp_filename  # Use the temporary file for saving

        # Act
        library.save_library()

        # Assert
        with open(temp_filename, 'r') as file:
            data = json.load(file)
            expected_data = [book1.to_dict(), book2.to_dict()]
            self.assertEqual(data, expected_data, "The saved library data does not match the expected data")

        # Clean up
        os.remove(temp_filename)

    def test_load_function(self):
        # Arrange
        book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "Fantasy")
        book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy")
        library = Library()
        library.add_book(book1)
        library.add_book(book2)

        # Act
        library.load_library()

        # Assert
        with open("library.json", 'r') as file:
            data = json.load(file)
            self.assertEqual(library.to_dict(), data, "The saved library data does not match the expected data")
