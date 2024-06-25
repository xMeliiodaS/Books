from flask import Flask, request, render_template, redirect, url_for, flash
from library import Library
from book import Book



class App:
    def __init__(self):
        """
        Initialize the LibraryApp class with Flask app and Library instance.
        """
        self.app = Flask(__name__)
        self.app.secret_key = 'your_secret_key'  # Required for flashing messages
        self.library = Library()
        self.setup_routes()

    def setup_routes(self):
        """
        Setup Flask routes for the application.
        """
        self.app.add_url_rule('/', view_func=self.index)
        self.app.add_url_rule('/books', view_func=self.add_books, methods=['GET', 'POST'])
        self.app.add_url_rule('/edit/<title>', view_func=self.edit_book, methods=['GET', 'POST'])
        self.app.add_url_rule('/delete/<title>', view_func=self.delete_book)
        self.app.add_url_rule('/search', view_func=self.search_books, methods=['GET'])

    @staticmethod
    def index():
        """
        Render the index.html template for the home page.

        Returns:
        - str: Rendered HTML content for index page.
        """
        return render_template('index.html')

    def add_books(self):
        """
        Handle GET (list books) and POST (add book) requests for the books page.

        Returns:
        - Union[str, List[Dict[str, Union[str, int]]]]: Rendered HTML content for books page or list of books.
        """
        if request.method == 'POST':
            try:
                data = request.form
                title = data['title'].strip()  # Remove leading/trailing whitespace
                author = data['author'].strip()  # By the name of the input. name="author"
                year = int(data['year'].strip())
                genre = data['genre'].strip()

                if not title or not author or not year or not genre:
                    flash('All fields are required.', 'error')
                else:
                    book = Book(title, author, year, genre)
                    self.library.add_book(book)
                    flash('Book added successfully!', 'success')
                    return redirect(url_for('books'))

            except ValueError:
                flash('Invalid input for year.', 'error')
            except Exception as e:
                flash(f'Error occurred: {str(e)}', 'error')

        return render_template('books.html', books=self.library.list_books())

    def edit_book(self, title):
        """
        Handle GET (render edit form) and POST (update book details) requests for editing a book.

        Args:
        - title (str): Title of the book to edit.

        Returns:
        - Rendered HTML content for edit book page or redirect to books page.
        """
        book = next((book for book in self.library.books if book.title == title), None)
        if not book:
            flash('Book not found.', 'error')
            return redirect(url_for('books'))

        if request.method == 'POST':
            try:
                data = request.form
                new_title = data.get('new_title').strip()
                author = data.get('author').strip()
                year = int(data.get('year').strip())
                genre = data.get('genre').strip()

                new_details = {
                    "title": new_title,
                    "author": author,
                    "publication_year": year,
                    "genre": genre
                }
                self.library.edit_book(title, new_details)
                flash('Book updated successfully!', 'success')
                return redirect(url_for('books'))

            except ValueError:
                flash('Invalid input for year.', 'error')
            except Exception as e:
                flash(f'Error occurred: {str(e)}', 'error')

        return render_template('edit_book.html', book=book)

    def delete_book(self, title):
        """"
        Handle deleting a book from the library.

        Args:
        - title (str): Title of the book to delete.

        Returns:
        - redirect: Redirect to books page after deleting the book.
        """
        try:
            self.library.delete_book(title)
            flash('Book deleted successfully!', 'success')
        except Exception as e:
            flash(f'Error occurred: {str(e)}', 'error')

        return redirect(url_for('books'))

    def search_books(self):
        """
        Handle search functionality for books based on title.

        Returns:
        - Rendered HTML content with filtered books based on search query.
        """
        query = request.args.get('search')
        if query:
            filtered_books = self.library.search_books(query)
        else:
            filtered_books = self.library.list_books()

        return render_template('books.html', books=filtered_books)

    def run(self):
        """
        Start the Flask application.
        """
        self.app.run(debug=True)


if __name__ == '__main__':
    app = App()
    app.run()
