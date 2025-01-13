import products
import store

# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
    ]
best_buy = store.Store(product_list)


def start(store):
    """
    creates the user interface/menu
    """
    while True:
        print("\n⭐ 🤑 W e l c o m e  t o  B e s t  B u y ! 🤑 ⭐")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            print("\nProducts in store:")
            for product in store.get_all_products():
                print(product.show())

        elif choice == 2:
            print(f"\nTotal quantity in store: {store.get_total_quantity()} items")

        elif choice == 3:
            print("\nMake an order: 💸")
            products = store.get_all_products()
            shopping_list = []

            for index, product in enumerate(products, start=1):
                print(f"{index}. {product.show()}")

            print("\nWhen you want to finish the order, enter an empty text.")
            while True:
                product_number = input("Which product # do you want? ").strip()
                if not product_number:
                    break

                try:
                    product_number = int(product_number)
                    if 1 <= product_number <= len(products):
                        quantity = int(input("How many do you want? ").strip())
                        shopping_list.append((products[product_number - 1], quantity))
                    else:
                        print("Invalid product number. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid product number or quantity.")
                    continue

            try:
                if shopping_list:
                    total_cost = store.order(shopping_list)
                    print(f"\nOrder placed successfully! Total cost: ${total_cost:.2f}")
                else:
                    print("\nNo items were ordered.")
            except Exception as e:
                print(f"Error: {e}")


        elif choice == 4:
            print("\nThank you for visiting ⭐ 🤑 B e s t  B u y ! 🤑 ⭐")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    start(best_buy)
