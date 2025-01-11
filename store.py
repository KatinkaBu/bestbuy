class Store:
    def __init__(self, products):
        """Initialize the store with a list of products."""
        self.products = products

    def add_product(self, product):
        """Add a new product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        if product in self.products:
            self.products.remove(product)
        else:
            print("Product not found in the store.")

    def get_total_quantity(self) -> int:
        """Return the total quantity of all items in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> list:
        """Return all products in the store that are active."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        """
        Processes an order for a list of products and quantities.

        Args:
            shopping_list (list of tuples): Each tuple contains a product instance and quantity to buy.

        Returns:
            float: The total price of the order.

        Raises:
            Exception: If a product does not have enough quantity to fulfill the order.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception(f"The product '{product.name}' is not available in the store.")
            try:
                total_price += product.buy(quantity)
            except Exception as e:
                raise Exception(f"Failed to process the order for '{product.name}': {str(e)}")
        return total_price