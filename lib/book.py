#!/usr/bin/env python3

#!/usr/bin/env python3

class Book:
    """Represents a book in the bookstore with a title, page count, and reading actions."""

    def __init__(self, title, page_count):
        """Initialize a Book with a title and page count.

        Args:
            title (str): The title of the book.
            page_count (int): The total number of pages in the book.
        """
        self.title = title
        self.page_count = page_count  # Uses the property setter for validation

    @property
    def page_count(self):
        """Return the current page count."""
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """Set page count, ensuring it is an integer.

        Prints an error message if the value is not an integer.
        """
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        """Simulate turning a page in the book."""
        print("Flipping the page...wow, you read fast!")
    
        