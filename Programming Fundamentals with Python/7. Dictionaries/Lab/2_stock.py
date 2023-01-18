quantities = input().split()
bakery = {}
for i in range(0, len(quantities), 2) :
    key = quantities[i]
    value = int(quantities[i + 1])
    bakery[key] = value
quantity = input().split()
for product in quantity:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

