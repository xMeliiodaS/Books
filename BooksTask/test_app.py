import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Run once before all tests
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
    driver.get("http://127.0.0.1:5000/")  # Change this to the appropriate URL

    # Click on "Manage Books" once before all tests
    driver.find_element(By.LINK_TEXT, "Manage Books").click()
    time.sleep(1)  # Wait for 1 second

    yield driver
    driver.quit()

    # Empty the JSON file after all tests
    with open("library.json", "w") as file:
        json.dump([], file)


# Run before each test
def setup_function():
    """
    Function to run before each test to ensure the library is empty.
    """
    with open("library.json", "w") as file:
        json.dump([], file)


def test_add_book(browser):
    """
    Test adding a book to the library.
    """
    # Add a new book
    browser.find_element(By.ID, "title").send_keys("Test Book")
    browser.find_element(By.ID, "author").send_keys("Test Author")
    browser.find_element(By.ID, "year").send_keys("2024")
    browser.find_element(By.ID, "genre").send_keys("Test Genre")
    browser.find_element(By.CLASS_NAME, "add-btn").click()
    time.sleep(1)  # Wait for 1 second

    # Check if the book was added successfully
    assert "Book added successfully!" in browser.page_source


def test_edit_book(browser):
    """
    Test editing a book in the library.
    """
    # Add a book to edit
    #   test_add_book(browser)

    # Edit the book
    browser.find_element(By.LINK_TEXT, "Edit").click()
    time.sleep(1)  # Wait for 1 second

    title_field = browser.find_element(By.ID, "new_title")
    title_field.clear()
    title_field.send_keys("Updated Test Book")

    browser.find_element(By.CLASS_NAME, "update-btn").click()
    time.sleep(1)  # Wait for 1 second

    # Check if the book was updated successfully
    assert "Book updated successfully!" in browser.page_source


def test_delete_book(browser):
    """
    Test deleting a book from the library.
    """
    # Add a book to delete
    test_add_book(browser)

    # Delete the book
    browser.find_element(By.LINK_TEXT, "Delete").click()
    time.sleep(1)  # Wait for 1 second

    # Check if the book was deleted successfully
    assert "Book deleted successfully!" in browser.page_source


def test_search_book(browser):
    """
    Test searching for a book in the library.
    """
    # Add a book to search
    test_add_book(browser)

    # Search for the book
    search_field = browser.find_element(By.ID, "search")
    search_field.send_keys("Test Book")
    search_field.send_keys(Keys.RETURN)
    time.sleep(1)  # Wait for 1 second

    # Check if the book is displayed in the search results
    assert "Test Book" in browser.page_source
