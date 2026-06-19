!/usr/bin/env python3

class Book:
    """Represents an online book that a user can read in the bookstore."""

    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """Simulate the reader flipping to the next page."""
        print("Flipping the page...wow, you read fast!")
