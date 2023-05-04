# Simple example for debugging
# Contains (at least) two errors.

menu = {
    "eggs": 1.99,
    "bacon": 2.99,
    "sausage": 2.50,
    "hash browns": 1.99,
    "pancakes": 4.49,
    "toast": 1.49,
    "coffee": 1.49,
    "tea": 1.49,
    "orange juice": 2.59,
    "milk": 1.79,
}

orders = [
    ["coffee", "sausage", "toast", "eggs"],
    ["orange juice", "bacon", "bacon", "hash browns"],
    ["pancakes", "eggs" "tea", "milk", "toast", "bacon"],
]

total = 0
for order_num, order in enumerate(orders):
    order_total = 0
    for item in order:
        total += menu[item]
    print(f"Total for order #{order_num}: ${order_total:.2f}")

print(f"Total for all orders: ${total:.2f}")
