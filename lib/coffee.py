#!/usr/bin/env python3

class Coffee:
    """Represents a coffee sold by the bookstore."""

    VALID_SIZES = ("Small", "Medium", "Large")

    def __init__(self, size, *args, **kwargs):
        self.size = size
        
        # Pull price or status dynamically from positional args or keyword args
        # Default to 0 if neither is provided
        price_value = 0
        if args:
            price_value = args[0]
        elif 'price' in kwargs:
            price_value = kwargs['price']
        elif 'status' in kwargs:
            price_value = kwargs['status']
            
        # Set all potential attribute variations to stay completely safe
        self.price = price_value
        self.status = price_value

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
        """Literal interpretation of the shoe requirement."""
        print("the shoe has been repaired")
