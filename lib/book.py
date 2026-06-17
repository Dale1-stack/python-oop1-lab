!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        # Triggers the setter validation
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Validate that page_count is strictly an integer
        if not isinstance(value, int):
            print("page_count must be an integer")
            self._page_count = 0  # Fallback safe assignment
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

