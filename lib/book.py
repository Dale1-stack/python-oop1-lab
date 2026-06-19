!/usr/bin/env python3

class Book:
    """Represents an online book that a user can read in the bookstore."""

    def __init__(self, title: str, page_count: int):
        self.title = title
        # Triggers the setter validation immediately
        self.page_count = page_count 

    @property
    def page_count(self) -> int:
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Strict validation for whole-number page counts
        if isinstance(value, int) and not isinstance(value, bool):
            self._page_count = value
        else:
            print("page_count must be an integer")
            raise ValueError("page_count must be an integer")

    def turn_page(self):
        """Simulate the reader flipping to the next page."""
        print("Flipping the page...wow, you read fast!")
