# menu.py

MENU = {
    1: {"name": "Burger", "price": 80.00},
    2: {"name": "Pizza", "price": 150.00},
    3: {"name": "Fried Chicken", "price": 120.00},
    4: {"name": "Spaghetti", "price": 100.00},
    5: {"name": "French Fries", "price": 60.00},
    6: {"name": "Soft Drink", "price": 40.00}
}


def display_menu():
    print("\n========== RESTAURANT MENU ==========")

    for number, item in MENU.items():
        print(f"{number}. {item['name']:<20} ₱{item['price']:.2f}")

    print("0. Finish Order")
    print("=====================================")


def get_item(item_number):
    return MENU.get(item_number)