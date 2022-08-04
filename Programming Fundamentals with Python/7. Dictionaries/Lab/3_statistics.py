products = {}

command = input()
while command != "statistics":
    key, value = command.split(": ")
    if key in products:
        products[key] += int(value)
    else:
        products[key] = int(value)
    command = input()

print("Products in stock:")
for product in products:
    print(f"- {product}: {products[product]}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
