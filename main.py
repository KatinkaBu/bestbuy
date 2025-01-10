from products import Product

def main():
    # Create products
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    # Perform operations
    print(bose.buy(50))  # 12500.0
    print(mac.buy(100))  # 145000.0
    print(mac.is_active())  # False

    bose.show()  # Bose QuietComfort Earbuds, Price: 250, Quantity: 450
    mac.show()  # MacBook Air M2, Price: 1450, Quantity: 0 (deactivated)

    bose.set_quantity(1000)
    bose.show()  # Bose QuietComfort Earbuds, Price: 250, Quantity: 1000

if __name__ == "__main__":
    main()
