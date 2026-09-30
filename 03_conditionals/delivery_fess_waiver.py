order_amount = int(input("What's the order amount ?"))

# used ternary operator here
delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fee charged is : {delivery_fees}")