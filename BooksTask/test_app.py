import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture(scope="module")
def browser():
    """
    Fixture to create a Selenium WebDriver instance for the browser.
    """
    driver = webdriver.Chrome()  # Create an instance of Chrome WebDriver
    driver.get("http://127.0.0.1:5000/")  # Navigate to the URL of the web application
    yield driver  # Yield the WebDriver instance for use in tests
    driver.quit()  # Quit the WebDriver after the tests are done


def test_add_book(browser):
    """
    Test adding a new book to the library
    :param browser:
    :return:
    """
    # Click on the "Manage Books" link
    browser.find_element(By.LINK_TEXT, "Manage Books").click()
    time.sleep(1)  # Wait for 1 second

    # Fill in the form fields with the book details
    browser.find_element(By.ID, "title").send_keys("Test Book")
    browser.find_element(By.ID, "author").send_keys("Test Author")
    browser.find_element(By.ID, "year").send_keys("2024")
    browser.find_element(By.ID, "genre").send_keys("Test Genre")

    # Click the "Add Book" button
    browser.find_element(By.CLASS_NAME, "add-btn").click()
    time.sleep(1)

    assert "Book added successfully!" in browser.page_source
