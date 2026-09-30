# main.py

from menu import display_menu, get_item
from order import add_item, calculate_total
from receipt import display_receipt


def main():
    print("=====================================")
    print("       RESTAURANT ORDERING SYSTEM    ")
    print("=====================================")

    customer_name = input("Enter customer name: ")

    order = []

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 0:
                break

            item = get_item(choice)

            if item is None:
                print("Invalid menu choice. Please try again.")
                continue

            quantity = int(input(f"Enter quantity for {item['name']}: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

            add_item(order, item, quantity)

            print(
                f"{quantity} x {item['name']} "
                "added to your order."
            )

        except ValueError:
            print("Please enter a valid number.")

    if len(order) == 0:
        print("\nNo items were ordered.")
        print("Thank you!")
        return

    total = calculate_total(order)

    display_receipt(
        customer_name,
        order,
        total
    )


if __name__ == "__main__":
    main()