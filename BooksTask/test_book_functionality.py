import unittest

from book import Book


class TestBookFunctionality(unittest.TestCase):

    def test_update_book_function_equal(self):
        # Arrange
        book1 = Book("Harry", "M7mod", 2001, "Magic")

        # Act
        book1.update("Potter", "Shibel", 2002, "Fantasy")

        # Assert
        self.assertEqual("Potter", book1.title, "Title was not updated correctly")
        self.assertEqual("Shibel", book1.author, "Author was not updated correctly")
        self.assertEqual(2002, book1.publication_year, "Publication year was not updated correctly")
        self.assertEqual("Fantasy", book1.genre, "Genre was not updated correctly")

    def test_update_book_function_not_equal(self):
        # Arrange
        book1 = Book("Harry", "M7mod", 2001, "Magic")

        # Act
        book1.update("Potter", "Shibel", 2002, "Fantasy")

        # Assert
        self.assertNotEqual("Harry", book1.title, "Title should not be the old value")
        self.assertNotEqual("M7mod", book1.author, "Author should not be the old value")
        self.assertNotEqual(2001, book1.publication_year, "Publication year should not be the old value")
        self.assertNotEqual("Magic", book1.genre, "Genre should not be the old value")

    def test_init_book_function(self):
        # Act
        book1 = Book("Harry", "M7mod", 2001, "Magic")

        # Assert
        self.assertEqual("Harry", book1.title, "Title was not set correctly")
        self.assertEqual("M7mod", book1.author, "Author was not set correctly")
        self.assertEqual(2001, book1.publication_year, "Publication year was not set correctly")
        self.assertEqual("Magic", book1.genre, "Genre was not set correctly")

    def test_init_book_function_not_equal(self):
        # Act
        book1 = Book("Harry", "M7mod", 2001, "Magic")

        # Assert
        self.assertNotEqual(None, book1.title, "Title should not be None")
        self.assertNotEqual(None, book1.author, "Author should not be None")
        self.assertNotEqual(None, book1.publication_year, "Publication year should not be None")
        self.assertNotEqual(None, book1.genre, "Genre should not be None")

    def test_to_dict_function_equal(self):
        # Arrange
        book = Book("Harry", "M7mod", 2001, "Magic")

        expected_dict = {
            "title": "Harry",
            "author": "M7mod",
            "publication_year": 2001,
            "genre": "Magic"
        }

        # Act
        actual_dict = book.to_dict()

        # Assert
        self.assertEqual(expected_dict, actual_dict)

    def test_to_dict_function_not_equal(self):
        # Arrange
        book = Book("Harry", "M7mod", 2001, "Magic")

        expected_dict = {
            "title": "Potter",
            "author": "Shibel",
            "publication_year": 2002,
            "genre": "Fantasy"
        }

        # Act
        actual_dict = book.to_dict()

        # Assert
        self.assertNotEqual(expected_dict, actual_dict,
                            "The expected_dict representation of the book should not match the actual_dict")
