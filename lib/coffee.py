!/usr/bin/env python3

class Coffee:
    """Represents a coffee sold by the bookstore."""

    VALID_SIZES = ("Small", "Medium", "Large")

    def __init__(self, size: str, price: float):
        # Triggers the setter validation immediately
        self.size = size
        self.price = price

    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, value):
        # Strict validation against allowed sizes
        if value in Coffee.VALID_SIZES:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
            raise ValueError("size must be Small, Medium, or Large")

    def tip(self):
        """Thank the customer and add a $1 tip to the price."""
        print("This coffee is great, here’s a tip!")
        self.price += 1
