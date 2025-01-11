import products
from store import Store

def main():
    # Create a list of products
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    # Create the store instance with the product list
    store = Store(product_list)

    # Get all active products
    active_products = store.get_all_products()

    # Print the total quantity of all products in the store
    print("Total quantity in store:", store.get_total_quantity())

    # Place an order and print the total price
    try:
        total_price = store.order([(active_products[0], 1), (active_products[1], 2)])
        print(f"Total price of the order: {total_price} dollars.")
    except Exception as e:
        print(f"Order failed: {str(e)}")

if __name__ == "__main__":
    main()
