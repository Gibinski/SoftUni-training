orders = int(input())
total_price = 0
for order in range(orders):
    capsules_price = float(input())
    days = int(input())
    per_day = int(input())
    if capsules_price < 0.01 or capsules_price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif per_day < 1 or per_day > 2000:
        continue
    price = capsules_price * days * per_day
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price
print(f"Total: ${total_price:.2f}")
