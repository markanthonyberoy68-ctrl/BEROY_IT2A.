# order.py

def add_item(order, item, quantity):
    item_name = item["name"]
    price = item["price"]

    # Check if item already exists
    for ordered_item in order:
        if ordered_item["name"] == item_name:
            ordered_item["quantity"] += quantity
            return

    order.append({
        "name": item_name,
        "price": price,
        "quantity": quantity
    })


def calculate_total(order):
    total = 0

    for item in order:
        total += item["price"] * item["quantity"]

    return total