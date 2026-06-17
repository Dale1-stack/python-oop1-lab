!/usr/bin/env python3

class Coffee:
    """Represents a coffee item in the bookstore with a size, price, and tipping action."""

    # Valid size options for a coffee order
    VALID_SIZES = ["Small", "Medium", "Large"]

    def __init__(self, size, price):
        """Initialize a Coffee with a size and price.

        Args:
            size (str): The size of the coffee — must be Small, Medium, or Large.
            price (float): The price of the coffee.
        """
        self.size = size    # Uses the property setter for validation
        self.price = price

    @property
    def size(self):
        """Return the current size of the coffee."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the coffee size, ensuring it is one of the valid options.

        Prints an error message if the value is not Small, Medium, or Large.
        """
        if value not in self.VALID_SIZES:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    def tip(self):
        """Express appreciation for the coffee and add a $1 tip to the price."""
        print("This coffee is great, here\u2019s a tip!")
        self.price += 1