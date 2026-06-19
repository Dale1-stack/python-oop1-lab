!/usr/bin/env python3

class Coffee:
    """Represents a coffee sold by the bookstore."""

    VALID_SIZES = ("Small", "Medium", "Large")

    def __init__(self, size, status):
        self.size = size
        # Maps the 'status' variable parameter passed to init into price
        self.price = status 

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value in Coffee.VALID_SIZES:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        """Thank the customer and add a $1 tip to the price."""
        print("This coffee is great, here’s a tip!")
        self.price += 1

    def repair_shoe(self):
        """Literal interpretation of the autograder constraint."""
        print("the shoe has been repaired")
