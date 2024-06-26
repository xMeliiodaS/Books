import unittest

from book import Book


class TestBookFunctionality(unittest.TestCase):

    def test_update_book_function_equal(self):
        # Arrange
        book1 = Book("Harry", "M7mod", 2001, "Magic")

        # Act
        book1.update("Potter", "Shibel", 2002, "Fantasy")

        # Assert
        self.assertEqual("Potter", book1.title)
        self.assertEqual("Shibel", book1.author)
        self.assertEqual(2002, book1.publication_year)
        self.assertEqual("Fantasy", book1.genre)

    def test_update_book_function_not_equal(self):
        # Arrange
        book1 = Book("Harry", "M7mod", 2001, "Magic")

        # Act
        book1.update("Potter", "Shibel", 2002, "Fantasy")

        # Assert
        self.assertNotEqual("Harry", book1.title)
        self.assertNotEqual("M7mod", book1.author)
        self.assertNotEqual(2001, book1.publication_year)
        self.assertNotEqual("Magic", book1.genre)

    def test_init_book_function(self):
        # Arrange
        book1 = None

        # Act
        book1 = Book("Harry", "M7mod", 2001, "Magic")

        # Assert
        self.assertEqual("Harry", book1.title)
        self.assertEqual("M7mod", book1.author)
        self.assertEqual(2001, book1.publication_year)
        self.assertEqual("Magic", book1.genre)

    def test_init_book_function_not_equal(self):
        # Arrange
        book1 = Book(None, None, None, None)

        # Act
        book1 = Book("Harry", "M7mod", 2001, "Magic")

        # Assert
        self.assertNotEqual(None, book1.title)
        self.assertNotEqual(None, book1.author)
        self.assertNotEqual(None, book1.publication_year)
        self.assertNotEqual(None, book1.genre)