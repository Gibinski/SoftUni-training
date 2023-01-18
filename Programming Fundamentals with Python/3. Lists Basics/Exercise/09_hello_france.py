TICKET_COST = 150
collection_of_items = input().split("|")
budget = float(input())
basket = budget
profit = .0
price_list = []
for item in collection_of_items:
    items = item.split("->")
    type = items[0]
    price = float(items[1])
    filter_items = (
        basket >= price and (
            (type == "Clothes" and price <= 50) or
            (type == "Shoes" and price <= 35) or
            (type == "Accessories" and price <= 20.50)
        )
    )
    if filter_items:
        basket -= price
        profit += price * 0.4
        price *= 1.4 
        price_list.append(f"{price:.2f}")
        
print(" ".join(price_list))
print(f"Profit: {profit:.2f}")
if budget + profit >= TICKET_COST:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")