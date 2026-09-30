# restaurant.py


class RestaurantOrderingSystem:

    def __init__(self):
        self.customer_name = ""
        self.order = []

        self.menu = {
            1: {"name": "Burger", "price": 80.00},
            2: {"name": "Pizza", "price": 150.00},
            3: {"name": "Fried Chicken", "price": 120.00},
            4: {"name": "Spaghetti", "price": 100.00},
            5: {"name": "French Fries", "price": 60.00},
            6: {"name": "Soft Drink", "price": 40.00}
        }

    def get_customer_name(self):
        self.customer_name = input("Enter customer name: ")

    def display_menu(self):
        print("\n========== RESTAURANT MENU ==========")

        for number, item in self.menu.items():
            print(
                f"{number}. "
                f"{item['name']:<20} "
                f"₱{item['price']:.2f}"
            )

        print("0. Finish Order")
        print("=====================================")

    def add_item(self, choice, quantity):
        item = self.menu.get(choice)

        if item is None:
            print("Invalid menu choice.")
            return False

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return False

        # Check if the item already exists
        for ordered_item in self.order:
            if ordered_item["name"] == item["name"]:
                ordered_item["quantity"] += quantity
                return True

        self.order.append({
            "name": item["name"],
            "price": item["price"],
            "quantity": quantity
        })

        return True

    def calculate_total(self):
        total = 0

        for item in self.order:
            total += item["price"] * item["quantity"]

        return total

    def display_receipt(self):
        total = self.calculate_total()

        print("\n")
        print("=====================================")
        print("          RESTAURANT RECEIPT         ")
        print("=====================================")
        print(f"Customer: {self.customer_name}")
        print("-------------------------------------")

        for item in self.order:
            subtotal = item["price"] * item["quantity"]

            print(
                f"{item['name']:<18} "
                f"x{item['quantity']:<3} "
                f"₱{subtotal:.2f}"
            )

        print("-------------------------------------")
        print(f"TOTAL:                  ₱{total:.2f}")
        print("=====================================")
        print("       Thank you for ordering!       ")
        print("=====================================")

    def run(self):
        print("=====================================")
        print("       RESTAURANT ORDERING SYSTEM    ")
        print("=====================================")

        self.get_customer_name()

        while True:
            self.display_menu()

            try:
                choice = int(input("Enter your choice: "))

                if choice == 0:
                    break

                if choice not in self.menu:
                    print("Invalid menu choice.")
                    continue

                quantity = int(
                    input(
                        f"Enter quantity for "
                        f"{self.menu[choice]['name']}: "
                    )
                )

                if self.add_item(choice, quantity):
                    print(
                        f"{quantity} x "
                        f"{self.menu[choice]['name']} "
                        "added to your order."
                    )

            except ValueError:
                print("Please enter a valid number.")

        if len(self.order) == 0:
            print("\nNo items were ordered.")
            print("Thank you!")
            return

        self.display_receipt()