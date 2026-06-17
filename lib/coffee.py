!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        # Triggers the setter validation
        self.size = size
        self.price = float(price)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        valid_sizes = ["Small", "Medium", "Large"]
        # Standardize case to handle minor user typos if needed, or check directly
        if value not in valid_sizes:
            print("size must be Small, Medium, or Large")
            self._size = "Medium"  # Fallback default assignment
        else:
            self._size = value

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1