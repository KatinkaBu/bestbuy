class Product:
    def __init__(self, name, price, quantity):
        #gpt
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input: name must not be empty, price and quantity must be non-negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        #gpt
        self.active = True

    def get_quantity(self):
        """
        Getter function for quantity. Returns the quantity (float).
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Setter function for quantity. If quantity reaches 0, deactivates the product.
        """
        #gpt
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        #muss ich das nochmal schreiben?
        self.quantity = quantity

        # Deactivate the product if quantity is 0
        if self.quantity == 0:
            self.active = False


    def is_active(self):
        """
        Getter function for active. Returns True if the product is active, otherwise False.
        """
        return self.active


    def activate(self):
        """
        Activates the product.
        """
        self.active = True


    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False


    def show(self):
        """
        Returns a string that represents the product. E.g. "MacBook Air M2, Price: 1450, Quantity: 100"
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem (when? think about it), raises an Exception.
        """
        #gpt
        if not self.active:
            raise Exception("Cannot purchase an inactive product.")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if quantity > self.quantity:
            raise Exception(f"Not enough stock. Available quantity: {self.quantity}")

        # Calculate the total price
        total_price = quantity * self.price

        # Update the quantity of the product
        self.quantity -= quantity

        # Deactivate the product if quantity reaches 0
        if self.quantity == 0:
            self.deactivate()

        return total_price


