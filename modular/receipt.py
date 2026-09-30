# receipt.py

def display_receipt(customer_name, order, total):
    print("\n")
    print("=====================================")
    print("          RESTAURANT RECEIPT         ")
    print("=====================================")
    print(f"Customer: {customer_name}")
    print("-------------------------------------")

    for item in order:
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