from products import Product

class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        """
        Adds a product to the store.
        """
        if isinstance(product, Product):
            self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """
        Returns the total quantity of all products in the store.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """
        Returns all active products in the store.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """
        Takes a list of (Product, quantity) tuples, buys them, and returns the total price.
        """
        total_price = 0
        for product, quantity in shopping_list:
            if isinstance(product, Product) and product.is_active() and product.get_quantity() >= quantity:
                total_price += product.buy(quantity)
            else:
                raise Exception(f"Product {product.name} not available in the required quantity or not active.")
        return total_price
