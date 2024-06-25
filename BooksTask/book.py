class Book:

    def __init__(self, title, author, publication_year, genre):
        """
        Initialize a Book object with title, author, publication year, and genre.

        Args:
        - title (str): The title of the book.
        - author (str): The author of the book.
        - publication_year (int): The year the book was published.
        - genre (str): The genre of the book.
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre

    def update(self, title=None, author=None, publication_year=None, genre=None):
        """
        Update the attributes of the book if new values are provided.

        Args:
        - title (str, optional): New title of the book.
        - author (str, optional): New author of the book.
        - publication_year (int, optional): New publication year of the book.
        - genre (str, optional): New genre of the book.
        """
        if title:
            self.title = title
        if author:
            self.author = author
        if publication_year:
            self.publication_year = publication_year
        if genre:
            self.genre = genre

    def to_dict(self):
        """
        Convert the Book object to a dictionary representation.

        Returns:
        - dict: Dictionary containing the attributes of the book.
        """
        return {
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "genre": self.genre
        }
